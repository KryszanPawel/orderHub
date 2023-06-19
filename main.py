import pandas as pd
import os

import extractor
from docToPdf import DocToPDF
from extractor import Extractor

if __name__ == "__main__":

    # GET LIST OF ORDERS
    listOfFiles = os.listdir("toRead")
    listOfFiles = [fileName for fileName in listOfFiles
                   if fileName.lower().endswith(".docx")
                   or fileName.lower().endswith(".doc")]

    # CREATE OUTPUT DATAFRAME
    outputDf = pd.DataFrame()
    orderList = []

    for document in listOfFiles:
        print(document)
        file = DocToPDF("toRead/" + document).convertToPDF()

        # CREATE EXTRACTOR INSTANCE
        documentData = Extractor(file)

        # EXTRACT ORDER NUMBER

        orderNumber = documentData.extractOrderNumber()

        # EXTRACT TABLES AS DATAFRAMES

        tables = documentData.extractTables()
        # print(tables[0]. )
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
                      f"j.m.: Szt."
                      f"wydano: {table.iloc[i][3].strip()} "
                      f"cena: {table.iloc[i][5].strip()} "
                      f"wartość: {table.iloc[i][6].strip()}"
                      f"nr zlecenia: {orderNumber}")

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
    os.remove("output.pdf")
    orderList.append(lastLine)
    outputDf = pd.DataFrame(orderList)
    outputDf.to_excel("output.xlsx",
                      sheet_name='Sheet_name_1')
