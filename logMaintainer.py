import os
from datetime import datetime

LOG_DIR: str = "log"

# INITIAL LOG HEADER
INFO_STRING: str = \
    " -------------------- \n" + \
    "| Document read log: |\n" + \
    " -------------------- \n"


def createLogDir() -> None:
    """Create log dir if one does not exist"""
    if "log" not in os.listdir():
        os.mkdir(LOG_DIR)
        with open(f"{LOG_DIR}\\log.txt", "w") as logFile:
            logFile.writelines(INFO_STRING)


def extractLogData() -> tuple:
    """Extract number of entries and content from log file"""
    with open(f"{LOG_DIR}\\log.txt", "r") as logFile:
        logFile.seek(0)
        fileOutput: list = logFile.readlines()
        logNo: int = len(
            [_ for _ in fileOutput
             if _.replace("\n", "").endswith(">")]
        ) + 1
        return logNo, fileOutput


def writeToLogFile(fileOutput: list[str]) -> None:
    """Override data in log file"""
    # DELETE LAST EMPTY LINE
    fileOutput[-1] = fileOutput[-1].replace("\n", "")
    with open(f"{LOG_DIR}\\log.txt", "w") as logFile:
        logFile.writelines(fileOutput)


class LogMaintainer:
    """Create new log entry"""

    def __init__(self, startTime, endTime, numberOfFilesRead: int):
        self.newEntry: dir = {
            "start": startTime,
            "end": endTime,
            "amountOfFiles": numberOfFilesRead
        }
        self.timeString: str = str(self.newEntry['end'] - self.newEntry["start"])

    def createNewEntry(self) -> None:
        """Create output of log entry to file"""
        self.addEntryToFile()
        # PRINT A RESULT
        print("\n")
        print(" " + "-" * 28 + " ")
        print(f"|  Log -> {self.newEntry['amountOfFiles']} files in %.2fs  |"
              % float(self.timeString))
        print(" " + "-" * 28 + " ")

    def addEntryToFile(self) -> None:
        """Writes new entry to log file if it exists,
        otherwise create new log/log.txt file"""
        # CREATE LOG DIR AND LOG.TXT IF IT DOES NOT EXIST
        createLogDir()

        logNo: int
        fileOutput: list

        # EXTRACT EXISTING DATA FROM LOG
        logNo, fileOutput = extractLogData()

        # FORMAT NEW ENTRY
        date: str = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        entry: str = f"%s -> %d files in %.2fs" % (
            date,
            self.newEntry['amountOfFiles'],
            float(self.timeString))

        entry = "{0:<50}".format(entry) + "<LOG NO: %d>\n" % logNo

        # INSERT ENTRY AS FIRST RECORD
        fileOutput = fileOutput[:3] + [entry] + fileOutput[3:]

        # WRITE TO FILE
        writeToLogFile(fileOutput)
