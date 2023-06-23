import pandas as pd
from time import time
import docGetter
import os
from docToPdf import DocToPDF
from extractor import Extractor
from logMaintainer import LogMaintainer
import sys

if __name__ == "__main__":

    # GET LIST OF ORDERS
    listOfFiles = docGetter.getFiles()[:5]

    # CREATE LIT TO BE CONVERTED TO DATAFRAME
    orderList = []
    # print(listOfFiles)
    # sys.stdout.flush()
    # sys.exit()

    fileCounter = 0
    finalCounter = len(listOfFiles)
    start = time()

    for document in listOfFiles:
        fileCounter += 1

        print(f"<{fileCounter}/{finalCounter}> {document}")
        sys.stdout.flush()

        file = DocToPDF("./tableReader/toRead/" + document).convertToPDF()

        # CREATE EXTRACTOR INSTANCE
        documentData = Extractor(file)

        # EXTRACT ORDER NUMBER

        orderNumber = documentData.extractOrderNumber()

        # EXTRACT TABLES AS DATAFRAMES

        tables = documentData.extractTables()
        for table in tables:
            for i in range(len(table)):
                if i == 0:
                    continue

                line = {
                    "l.p": i,
                    "kod towaru": table.iloc[i][1].strip(),
                    "detal": table.iloc[i][2].strip(),
                    "zdysponowano": table.iloc[i][3].strip(),
                    "j.m.": "Szt.",
                    "wydano": table.iloc[i][3].strip(),
                    "cena": table.iloc[i][5].strip(),
                    "wartość": table.iloc[i][6].strip(),
                    "nr zlecenia": orderNumber,
                    "uwagi": "",
                }
                orderList.append(line)

                print(f"kod towaru: {table.iloc[i][1].strip()} "
                      f"detal: {table.iloc[i][2].strip()} "
                      f"zdysponowano: {table.iloc[i][3].strip()} "
                      f"j.m.: Szt. "
                      f"wydano: {table.iloc[i][3].strip()} "
                      f"cena: {table.iloc[i][5].strip()} "
                      f"wartość: {table.iloc[i][6].strip()} "
                      f"nr zlecenia: {orderNumber}")
                sys.stdout.flush()

            emptyLine = {
                "l.p": "",
                "kod towaru": "",
                "detal": "",
                "zdysponowano": "",
                "j.m.": "",
                "wydano": "",
                "cena": "",
                "wartość": "",
                "uwagi": "",
            }
            orderList.append(emptyLine)

    orderList.pop()
    lastLine = {
        "l.p": "",
        "kod towaru": "KONIEC",
        "detal": "",
        "zdysponowano": "",
        "j.m.": "",
        "wydano": "",
        "cena": "",
        "wartość": "",
        "uwagi": "KONIEC",
    }
    os.remove(file)
    orderList.append(lastLine)

    # CREATE DATAFRAME AND CONVERT LIST
    outputDf = pd.DataFrame(orderList)
    outputDf.to_excel("./output.xlsx",
                      sheet_name='Sheet_name_1')

    end = time()

    # ADD LOG ENTRY
    LogMaintainer(start, end, fileCounter).createNewEntry()
