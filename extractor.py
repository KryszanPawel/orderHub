from pypdf import PdfReader
import camelot

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
        return tables
