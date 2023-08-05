"""Copyright © 2022 Burrus Financial Intelligence, Ltda. (hereafter, BFI) Permission to include in application
software or to make digital or hard copies of part or all of this work is subject to the following licensing
agreement.
BFI Software License Agreement: Any User wishing to make a commercial use of the Software must contact BFI
at jacques.burrus@bfi.lat to arrange an appropriate license. Commercial use includes (1) integrating or incorporating
all or part of the source code into a product for sale or license by, or on behalf of, User to third parties,
or (2) distribution of the binary or source code to third parties for use with a commercial product sold or licensed
by, or on behalf of, User. """

import time
import multiprocessing
import datetime
import pandas
from enum import Enum
from pacifico_devel.util.aws import EC2, S3  # from ..aws import EC2, S3
from pacifico_devel.util.cfg import Configuration  # from ..cfg import Configuration
from pacifico_devel.util import Dates  # from .. import Dates

class Status(Enum):
    Started = 0
    Ended = 1
    Failed = 2

    def getString(self):
        return self.name

    @classmethod
    def fromString(cls, string):
        return cls[string]

    def isFinished(self):
        if self in [Status.Ended, Status.Failed]:
            return True
        return False

class LoadBalancer:
    cooldownInSeconds = 180
    errorInSeconds = 10

    @staticmethod
    def getTimestamp():
        dateNow = datetime.datetime.now()
        timestamp = Dates.getDateTimeTimestamp(dateNow)
        return timestamp

    @staticmethod
    def getTimestampId():
        dateNow = datetime.datetime.now()
        timestampExcel = Dates.getExcelDate(dateNow)
        timestampId = int(timestampExcel * 1000000000)
        return timestampId

    @staticmethod
    def _checkIfBiggerInList(value, list):
        for x in list:
            if value >= x:
                return False
        return True

    @staticmethod
    def stopInstance(instanceId, awsAccessKey, awsSecretKey, force=False):
        computerStaticInstanceId = Configuration.get('COMPUTER_STATIC_2_INSTANCE_ID')
        if instanceId != computerStaticInstanceId or force:
            EC2.stopInstace(instanceId, awsAccessKey, awsSecretKey)


    @staticmethod
    def notifyStart(instanceId):
        processId = LoadBalancer.getTimestampId()
        t = multiprocessing.Process(target=LoadBalancer._notifyStart, args=(processId, instanceId,), daemon=False)
        t.start()
        return processId

    @staticmethod
    def _notifyStart(processId, instanceId):
        scheduleFile = LoadBalancer.getScheduleFile()
        timestamp = LoadBalancer.getTimestamp()
        status = Status.Started.getString()
        # Add start to schedule (invalidate previous stops)
        scheduleFile = LoadBalancer._updateOrAddRowToFile(scheduleFile, processId, instanceId, timestamp, status)
        # Clean older than a month
        scheduleFile = LoadBalancer.cleanScheduleFile(scheduleFile)
        # Update schedule file
        LoadBalancer.uploadScheduleFile(scheduleFile)
        print(f'notifyStart : {processId, instanceId}')
        print(scheduleFile)
        print(f'notifyStart {"*" * 10}')

    @staticmethod
    def notifyStop(processId, instanceId):
        t = multiprocessing.Process(target=LoadBalancer._notifyStop, args=(processId, instanceId,), daemon=False)
        t.start()

    @staticmethod
    def notifyEnd(processId, instanceId):
        t = multiprocessing.Process(target=LoadBalancer._notifyEnd, args=(processId, instanceId,), daemon=False)
        t.start()

    @staticmethod
    def notifyFailure(processId, instanceId):
        t = multiprocessing.Process(target=LoadBalancer._notifyFailure, args=(processId, instanceId,), daemon=False)
        t.start()

    @staticmethod
    def _notifyStop(processId, instanceId):
        LoadBalancer._notifyEnd(processId, instanceId)
        # Wait the cooldown period
        time.sleep(LoadBalancer.cooldownInSeconds)
        # Actually shutdown if it's valid
        LoadBalancer.executeStop(instanceId)
        print(f'notifyStop : {processId, instanceId}')

    @staticmethod
    def _notifyEnd(processId, instanceId):
        scheduleFile = LoadBalancer.getScheduleFile()
        timestamp = LoadBalancer.getTimestamp()
        status = Status.Ended.getString()
        # Add stop to schedule
        scheduleFile = LoadBalancer._updateOrAddRowToFile(scheduleFile, processId, instanceId, timestamp, status)
        # Update schedule file
        LoadBalancer.uploadScheduleFile(scheduleFile)
        print(f'notifyEnd : {processId, instanceId}')
        print(scheduleFile)
        print(f'notifyEnd {"*" * 10}')

    @staticmethod
    def _notifyFailure(processId, instanceId):
        scheduleFile = LoadBalancer.getScheduleFile()
        timestamp = LoadBalancer.getTimestamp()
        status = Status.Failed.getString()
        # Add stop to schedule
        scheduleFile = LoadBalancer._updateOrAddRowToFile(scheduleFile, processId, instanceId, timestamp, status)
        # Update schedule file
        LoadBalancer.uploadScheduleFile(scheduleFile)
        print(f'notifyFailure : {processId, instanceId}')
        print(scheduleFile)
        print(f'notifyFailure {"*" * 10}')

    @staticmethod
    def executeStop(instanceId):
        awsAccessKey = Configuration.get('AWS_ACCESS_KEY')
        awsSecretKey = Configuration.get('AWS_SECRET_KEY')
        # Check schedule
        instanceIsOn = EC2.isInstanceRunning(instanceId, awsAccessKey, awsSecretKey)
        if instanceIsOn:
            try:
                scheduleFile = LoadBalancer.getScheduleFile()
                relevantRows = scheduleFile.loc[scheduleFile['instanceId'] == instanceId]
                status = relevantRows['status'].unique()
                noOtherProcessesRunning = Status.Started.getString() not in status
                timestamps = relevantRows['timestamp'].unique()
                timedeltas = [datetime.datetime.now() - Dates.getDateTimeFromTimestamp(timestamp) for timestamp in timestamps]
                coolDownDelta = datetime.timedelta(seconds=(LoadBalancer.cooldownInSeconds - LoadBalancer.errorInSeconds))
                coolDownEnded = LoadBalancer._checkIfBiggerInList(coolDownDelta, timedeltas)
                isShutdownValid = noOtherProcessesRunning and coolDownEnded
                print(f'isShutdownValid: {isShutdownValid}')
                if isShutdownValid:  # If valid, shutdown
                    LoadBalancer.stopInstance(instanceId, awsAccessKey, awsSecretKey)
            except Exception as e:
                print(f'Error with schedule file: {str(e)}')
                LoadBalancer.stopInstance(instanceId, awsAccessKey, awsSecretKey)  # If file fails just stop the instance

    @staticmethod
    def _updateOrAddRowToFile(scheduleFile, processId, instanceId, timestamp, status):
        if instanceId in scheduleFile['instanceId'].values and processId in scheduleFile['processId'].values:
            scheduleFile.loc[scheduleFile['instanceId'] == instanceId, 'timestamp'] = timestamp
            scheduleFile.loc[scheduleFile['instanceId'] == instanceId, 'status'] = status
        else:
            row = LoadBalancer.buildScheduleRow(processId, instanceId, timestamp, status)
            scheduleFileNewRows = pandas.DataFrame([row])
            scheduleFile = pandas.concat([scheduleFile, scheduleFileNewRows], ignore_index=True)
        return scheduleFile

    @staticmethod
    def buildScheduleRow(processId, instanceId, timestamp, status):
        return {'processId': processId, 'instanceId': instanceId, 'timestamp': timestamp, 'status': status}

    @staticmethod
    def cleanScheduleFile(scheduleFile):
        aMonthAgo = datetime.date.today() - datetime.timedelta(days=30)
        scheduleFile['timestamp'] = scheduleFile['timestamp'].apply(lambda timestamp: Dates.getDateTimeFromTimestamp(timestamp))
        scheduleFile = scheduleFile.loc[scheduleFile['timestamp'] >= pandas.to_datetime(aMonthAgo)]
        scheduleFile['timestamp'] = scheduleFile['timestamp'].apply(lambda timestamp: Dates.getDateTimeTimestamp(timestamp))
        return scheduleFile

    # Downloading/Uploading Files

    @staticmethod
    def __getScheduleFilePaths():
        localPath = 'schedule.csv'
        bucketPath = f'LoadBalancer/{localPath}'
        bucket = 'bfi-cfg'
        return localPath, bucketPath, bucket

    @staticmethod
    def getScheduleFile():
        localPath, bucketPath, bucket = LoadBalancer.__getScheduleFilePaths()
        awsAccessKey = Configuration.get('AWS_ACCESS_KEY')
        awsSecretKey = Configuration.get('AWS_SECRET_KEY')
        S3.downloadFromBucket(bucketPath, localPath, bucket, read=False, awsAccessKey=awsAccessKey, awsSecretKey=awsSecretKey)
        schedule = pandas.read_csv(localPath)
        return schedule

    @staticmethod
    def uploadScheduleFile(schedule):
        localPath, bucketPath, bucket = LoadBalancer.__getScheduleFilePaths()
        awsAccessKey = Configuration.get('AWS_ACCESS_KEY')
        awsSecretKey = Configuration.get('AWS_SECRET_KEY')
        schedule = schedule.to_csv(index=False, sep=',', line_terminator='\n')
        S3.writeToBucket(schedule, localPath, bucket, bucketFilename=bucketPath, awsAccessKey=awsAccessKey, awsSecretKey=awsSecretKey)
