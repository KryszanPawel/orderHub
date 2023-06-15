from pypdf import PdfReader
import camelot
import pandas as pd


def flatten(table):
    flat_list = []
    for sublist in table:
        for item in sublist:
            flat_list.append(item)
    return flat_list


class Extractor:
    """Extracts information form PDF file"""

    def __init__(self, file):
        self.file = file

    def extractOrderNumber(self):
        reader = PdfReader(self.file)
        page = reader.pages[0]
        return page.extract_text().strip().split("\n")[0].split()[2]

    def extractTables(self):
        tables = [table.df for table in camelot.read_pdf(self.file)]

        # table extraction when 1 record
        if len(tables) == 0:
            title = ["Lp", "Nr artykułu", "Opis", "Ilość", "Jm", "Cena netto", "Wartość netto"]
            reader = PdfReader(self.file)
            page = reader.pages[0]
            table = page.extract_text().strip().split("\n")
            # filter essential data from table
            toRemove = []
            # remove data until table starts
            for index, item in enumerate(table):
                toRemove.append(item)
                if item.lower().startswith("lp"):
                    break
            for itemToRemove in toRemove:
                table.remove(itemToRemove)
            # remove data after table ends
            for index, item in enumerate(table):
                if item.lower().startswith("razem"):
                    table = table[:index]
                    break
            # create list of data and remove empty strings and whitespaces
            table = [item.strip() for item in table if item.strip() != ""]
            table = [item.split(" ") for item in table]
            table = flatten(table)
            table = [item for item in table if item != ""]

            # when part name is divided by spaces it needs to be joined
            if len(table) != len(title):
                tempTable = table[:2] + table[-4:]
                for position in tempTable:
                    table.remove(position)
                tempTable.insert(2, ' '.join(table))
                table = tempTable

            # create dataframe from table data
            data = [title, table]
            tables = [pd.DataFrame(data)]

        return tables
