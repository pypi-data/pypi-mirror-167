"""Copyright © 2022 Burrus Financial Intelligence, Ltda. (hereafter, BFI) Permission to include in application
software or to make digital or hard copies of part or all of this work is subject to the following licensing
agreement.
BFI Software License Agreement: Any User wishing to make a commercial use of the Software must contact BFI
at jacques.burrus@bfi.lat to arrange an appropriate license. Commercial use includes (1) integrating or incorporating
all or part of the source code into a product for sale or license by, or on behalf of, User to third parties,
or (2) distribution of the binary or source code to third parties for use with a commercial product sold or licensed
by, or on behalf of, User. """

import requests
import json
from ...cfg import Configuration  # from pacifico_devel.util.cfg import Configuration


class OpenFIGI:
    idTypes = {
        'ISIN': 'ID_ISIN',
        'CUSIP': 'ID_CUSIP',
        'Ticker': 'TICKER',
        'FIGI': 'ID_BB_GLOBAL'
    }

    def __init__(self):
        self.endpoint = 'https://api.openfigi.com'
        self.apiKey = Configuration.get('OPENFIGI_API_KEY')
        self.headers = {
            'Content-Type': 'application/json',
            'X-OPENFIGI-APIKEY': self.apiKey
        }
        self.mappingEndpoint = self.endpoint + '/v3/mapping'
        self.searchEndpoint = self.endpoint + '/v3/search'

    def getEndpoint(self):
        return self.endpoint

    def getApiKey(self):
        return self.apiKey

    def getHeaders(self):
        return self.headers

    def getMappingEndpoint(self):
        return self.mappingEndpoint

    def getSearchEndpoint(self):
        return self.searchEndpoint

    @classmethod
    def getIDTypes(cls):
        return cls.idTypes

    def getIDType(self, key):
        return self.getIDTypes().get(key)

    def search(self, key):
        payload = self._buildSearchPayload(key)
        response = requests.post(self.getSearchEndpoint(), data=payload, headers=self.getHeaders()).text
        response = json.loads(response)
        return self.__parseResponse(response)

    def _buildSearchPayload(self, key):
        payload = {
            "query": key,
        }
        return json.dumps(payload)

    def map(self, ISINs=None, CUSIPs=None, Tickers=None, FIGIs=None):
        if ISINs is None:
            ISINs = []
        if CUSIPs is None:
            CUSIPs = []
        if Tickers is None:
            Tickers = []
        if FIGIs is None:
            FIGIs = []
        searchList = ISINs + CUSIPs + Tickers + FIGIs
        mappingDict = self._buildMappingDict(ISINs, CUSIPs, Tickers, FIGIs)
        payload = self._buildMappingPayload(mappingDict)
        response = requests.post(self.getMappingEndpoint(), data=payload, headers=self.getHeaders()).text
        response = json.loads(response)
        responseDict = {}
        for search, searchResponse in zip(searchList, response):
            response = self.__parseResponse(searchResponse)
            if search in Tickers and response is None:
                response = self.search(search)
            responseDict.update({search: response})
        return responseDict

    def _buildMappingDict(self, ISINs, CUSIPs, Tickers, FIGIs):
        if not isinstance(ISINs, list):
            ISINs = [ISINs]
        if not isinstance(CUSIPs, list):
            CUSIPs = [CUSIPs]
        if not isinstance(Tickers, list):
            Tickers = [Tickers]
        if not isinstance(FIGIs, list):
            FIGIs = [FIGIs]
        mappingDict = {
            'ISIN': ISINs,
            'CUSIP': CUSIPs,
            'Ticker': Tickers,
            'FIGI': FIGIs
        }
        return mappingDict

    def _buildMappingPayload(self, mappingDict):
        # '[{"idType":"ID_WERTPAPIER","idValue":"851399"}]'
        payloadList = []
        for idType, idList in mappingDict.items():
            for specificId in idList:
                idDict = {"idType": self.getIDType(idType), "idValue": specificId}
                payloadList.append(idDict)
        return json.dumps(payloadList)

    def __parseResponse(self, response):
        if isinstance(response, str):
            response = json.loads(response)
        if "data" not in response.keys():
            return None
        reponseList = response.get("data")
        if reponseList == []:
            return None
        validResponse = reponseList[0]  # Select first hit
        return OpenFIGIResponse.fromDict(validResponse)

class OpenFIGIResponse:
    def __init__(self, figi, name, ticker, exchangeCode, compositeFigi, securityType, marketSector, shareClassFigi,
                 securityType2, securityDescription):
        self.figi = figi
        self.name = name
        self.ticker = ticker
        self.exchangeCode = exchangeCode
        self.compositeFigi = compositeFigi
        self.securityType = securityType
        self.marketSector = marketSector
        self.shareClassFigi = shareClassFigi
        self.securityType2 = securityType2
        self.securityDescription = securityDescription

    def getFIGI(self):
        return self.figi

    def getName(self):
        return self.name

    def getTicker(self):
        return self.ticker

    def getExchangeCode(self):
        return self.exchangeCode

    def getCompositeFigi(self):
        return self.compositeFigi

    def getSecurityType(self):
        return self.securityType

    def getMarketSector(self):
        return self.marketSector

    def getShareClassFigi(self):
        return self.shareClassFigi

    def getSecurityType2(self):
        return self.securityType2

    def getSecurityDescription(self):
        return self.securityDescription

    def getFamily(self):
        instrumentType = "NA"
        if self.getMarketSector() == "Corp":
            instrumentType = "BE"
        elif self.getMarketSector() == "Govt":
            instrumentType = "BT"
        elif self.getMarketSector() == "Equity":
                instrumentType = "AC"
                if "Mutual Fund" in self.getSecurityType2():
                    instrumentType = "CFM"
                if "ETF" in self.getName() or "ETF" in self.getSecurityType() or "ETP" in self.getSecurityType():
                    instrumentType = "ETF"
        return instrumentType

    def getJurisdiction(self):
        countryCode = self.getExchangeCode()
        if countryCode == "US":
            return "USA"
        if countryCode in ["LU", "NL", "IE", "FR", "DE", "IT", "ES", "AT", "SE"]:
            return "EU"
        if countryCode == "GB":
            return "UK"
        if countryCode == "JP":
            return "Japan"
        if countryCode in ["BR", "BZ"]:
            return "Brazil"
        if countryCode == "SG":
            return "Singapore"
        if countryCode == "BS":
            return "Bahamas"
        if countryCode == "VG":
            return "British Virgin Islands"
        if countryCode == "BM":
            return "British Bermuda"
        if countryCode == "BS":
            return "Bahamas"
        if countryCode == "KY":
            return "Cayman Islands"
        if countryCode == "PA":
            return "Panama"
        if countryCode == "HK":
            return "Hong Kong"
        if countryCode == "KR":
            return "South Korea"
        if countryCode in ['SANTIAGO', 'CHI']:
            return 'Chile'
        if countryCode == "MULT":
            return "World"
        if countryCode is None:
            countryCode = "NA"
        return countryCode

    def getNumeraire(self):
        return ''

    @classmethod
    def fromDict(cls, dict):
        figi = dict.get("figi")
        name = dict.get("name")
        ticker = dict.get("ticker")
        exchangeCode = dict.get("exchCode")
        compositeFigi = dict.get("compositeFIGI")
        securityType = dict.get("securityType")
        marketSector = dict.get("marketSector")
        shareClassFigi = dict.get("shareClassFIGI")
        securityType2 = dict.get("securityType2")
        securityDescription = dict.get("securityDescription")
        return cls(figi, name, ticker, exchangeCode, compositeFigi, securityType, marketSector, shareClassFigi, securityType2, securityDescription)

if __name__ == '__main__':
    openFIGI = OpenFIGI()
    ISINs = ['US4592001014', 'CL0002614940', 'caca']
    tickers = ['AAPL', 'TSLA', 'SANTANDER', 'SPY']
    y = openFIGI.map(ISINs, None, tickers)
    print(y)
    for x in y.values():
        if x is not None:
            print(x.__dict__)
