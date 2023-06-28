import pandas

def removeDuplicates(table):
     return table.groupby(['detal'], as_index=False)['wydano'].sum()


class OutputScanner:
    """Retrieve data from .xlsx file"""

    def __init__(self, xlsxFile):
        self.file = xlsxFile

    def getData(self):
        workbook = pandas.read_excel(self.file)
        return removeDuplicates(workbook)
