"""Copyright © 2022 Burrus Financial Intelligence, Ltda. (hereafter, BFI) Permission to include in application
software or to make digital or hard copies of part or all of this work is subject to the following licensing
agreement.
BFI Software License Agreement: Any User wishing to make a commercial use of the Software must contact BFI
at jacques.burrus@bfi.lat to arrange an appropriate license. Commercial use includes (1) integrating or incorporating
all or part of the source code into a product for sale or license by, or on behalf of, User to third parties,
or (2) distribution of the binary or source code to third parties for use with a commercial product sold or licensed
by, or on behalf of, User. """

import json
import pandas
import datetime
import requests
from .. import Strings, Dates  # from pacifico_devel.util import Strings, Dates
from ..aws import FTP  # from pacifico_devel.util.aws import FTP
from ..cfg import Configuration  # from pacifico_devel.util.cfg import Configuration
from .OpenFIGI import OpenFIGI  # from pacifico_devel.util.spellChecker.OpenFIGI import OpenFIGI

class SpellChecker:
    def __init__(self):
        self.openFIGI = OpenFIGI.OpenFIGI()
        self.ftpPath = 'backup/input/datawarehouse/sanexpedito/'

    def getOpenFIGI(self):
        return self.openFIGI

    def getFTPPath(self):
        return self.ftpPath

    def isISIN(self, key: str):
        key = key.upper()
        if len(key) != 12:
            return False
        elif not key[0].isalpha() or not key[1].isalpha():
            return False
        elif not all([character.isnumeric() for character in key[2:]]):
            return False
        else:
            return True

    def isCUSIP(self, key: str):
        key = key.upper()
        if len(key) != 9:
            return False
        elif not all([character.isnumeric() for character in key[:3]]):
            return False
        elif not all([character.isalnum() for character in key[3:8]]):
            return False
        elif not key[-1].isnumeric():
            return False
        else:
            return True

    def isFIGI(self, key: str):
        key = key.upper()
        if len(key) != 12:
            return False
        elif not all([character.isalpha() for character in key[:2]]):
            return False
        elif key[2] != 'G':
            return False
        elif not all([character.isalnum() for character in key[3:11]]):
            return False
        elif not key[-1].isnumeric():
            return False
        else:
            return True

    def classifyTickers(self, tickers, verbose=False):
        ISINs = []
        CUSIPs = []
        Tickers = []
        FIGIs = []
        for ticker in tickers:
            isISIN = self.isISIN(ticker)
            isCUSIP = self.isCUSIP(ticker)
            isFIGI = self.isFIGI(ticker)
            if verbose:
                print(f'{ticker}: {isISIN = } / {isCUSIP = } / {isFIGI = }')
            if isISIN:
                ISINs.append(ticker)
            elif isCUSIP:
                CUSIPs.append(ticker)
            elif isFIGI:
                FIGIs.append(ticker)
            else:
                Tickers.append(ticker)
        return ISINs, CUSIPs, Tickers, FIGIs

    def cleanTickers(self, tickers):
        # Standardize the list
        if isinstance(tickers, str):
            if '[' in tickers:
                tickers = json.loads(tickers)
            else:
                tickers = [tickers]
        # Actually clean the values
        cleanTickers = []
        for ticker in tickers:
            ticker = Strings.cleanString(ticker).strip()
            cleanTickers.append(ticker)
        return cleanTickers

    def checkForAlreadySearched(self, spellingDict, tickers):
        newTickers = []
        existing = {}
        for ticker in tickers:
            alreadySearched = spellingDict.get(ticker)
            if alreadySearched is None:
                newTickers.append(ticker)
            else:
                existing.update({ticker: alreadySearched})
        return newTickers, existing

    def addToRecovered(self, responses):
        rows = []
        addedFigis = []
        recoveredFile = self.getRecoveredFile()
        dateNow = Dates.getExcelDate(datetime.datetime.now())
        for key, response in responses.items():
            if response is not None:
                family = response.getFamily()
                jurisdiction = response.getJurisdiction()
                ticker = response.getTicker()

                numeraire = response.getNumeraire()
                figi = response.getFIGI()
                if figi not in addedFigis and ticker not in recoveredFile['Ticker BBG'].values:
                    isISIN = self.isISIN(key)
                    if isISIN:
                        ISIN = key
                    else:
                        ISIN = 'NA'
                    rows.append({'Mnemo': ISIN, 'Family': family, 'Jurisdiction': jurisdiction, 'Ticker BBG': ticker,
                                 'Date': dateNow, 'Numeraire BBG': numeraire, 'FIGI': figi})
                    addedFigis.append(figi)
            else:
                rows.append({'Mnemo': key, 'Family': '', 'Jurisdiction': '', 'Ticker BBG': 'not found', 'Date': dateNow,
                             'Numeraire BBG': '', 'FIGI': ''})
        dataframe = pandas.DataFrame(rows)
        newRecoveredFile = pandas.concat([recoveredFile, dataframe], ignore_index=True)
        # print(newRecoveredFile)
        self.updateRecoveredFile(newRecoveredFile)

    def getRecoveredFile(self):
        # unavailable = FTP.getCSVFileAsPandas(self.getFTPPath() + 'unavailable.csv', tmp=False)
        recovered = FTP.getCSVFileAsPandas(self.getFTPPath() + 'recovered.csv', tmp=False)
        return recovered

    def updateRecoveredFile(self, recoveredDataframe):
        FTP.uploadPandasAsCSV(recoveredDataframe, self.getFTPPath() + 'recovered.csv')

    def getSpellingFile(self):
        spelling = FTP.getFileAsString(self.getFTPPath() + 'spelling.json')
        return json.loads(spelling)

    def updateSpellingFile(self, spellingDict):
        spellingJson = json.dumps(spellingDict)
        FTP.uploadFileFromString(spellingJson, self.getFTPPath() + 'spelling.json')

    def runSanExpeditoAdmin(self):
        appRunnerBotsEndpoint = Configuration.get('APP_RUNNER_ENDPOINT')
        headers = {'Content-Type': 'application/json'}
        payload = {
            "bot name": "BotSanExpedito",
            "arguments": {
                "executionType": "admin"
            }
        }
        payload = json.dumps(payload)
        response = requests.post(appRunnerBotsEndpoint, data=payload, headers=headers).text
        print(f'SpellChecker: runSanExpeditoAdmin response -> {response}')

    def searchNewTickers(self, tickers, runSEAdmin):
        addedDict = {}
        # Classify tickers
        ISINs, CUSIPs, Tickers, FIGIs = self.classifyTickers(tickers)
        # Get OpenFIGI responses
        responses = self.getOpenFIGI().map(ISINs, CUSIPs, Tickers, FIGIs)
        for key, response in responses.items():
            if response is not None:
                # if key in Tickers and key != response.getTicker():
                #     print(f'Did you mean {response.getTicker()} ({response.getName()})')
                addedDict.update({key: (response.getTicker(), response.getName())})
        self.addToRecovered(responses)
        if runSEAdmin:
            self.runSanExpeditoAdmin()
        return addedDict

    def search(self, tickers, runSEAdmin=True):
        # Clean tickers
        tickers = self.cleanTickers(tickers)
        # Get spelling file
        spellingDict = self.getSpellingFile()
        # Check for already existing ones
        tickers, existingDict = self.checkForAlreadySearched(spellingDict, tickers)
        if tickers != []:
            addedDict = self.searchNewTickers(tickers, runSEAdmin)
            for ticker, added in addedDict.items():
                tickerFound, nameFound = added
                spellingDict.update({ticker: tickerFound})
        else:
            addedDict = {}
        # print(spellingDict)
        self.updateSpellingFile(spellingDict)
        return existingDict, addedDict

if __name__ == '__main__':
    pandas.set_option('display.max_rows', None)
    pandas.set_option('display.max_columns', None)
    pandas.set_option('display.width', 1000)
    pandas.set_option('display.colheader_justify', 'center')
    pandas.set_option('display.precision', 3)
    spellChecker = SpellChecker()
    tickers = 'PEN@IIA'  # ['US4592001014', 'CL0002614940']#, 'caca', 'AAPL', 'TSLA', 'SANTANDER', '037833100', '38259P508',
               # 'BBG000B9Y2J5', 'BBG000007X44']
    existingDict, addedDict = spellChecker.search(tickers)
    print(existingDict)
    print(addedDict)