import sys
import os
import _ctypes
import comtypes.client
import docx2pdf


class DocToPDF:
    """Converts .doc and .docx files to pdf"""

    def __init__(self, docFile):
        self.docFile = docFile

    def convertToPDF(self) -> str:
        outputFile = "output.pdf"
        if self.docFile.lower().endswith(".doc"):
            try:
                wdFormatPDF = 17
                in_file = os.path.abspath(self.docFile)
                out_file = os.path.abspath(outputFile)
                word = comtypes.client.CreateObject('Word.Application')
                doc = word.Documents.Open(in_file)
                doc.SaveAs(out_file, FileFormat=wdFormatPDF)
                doc.Close()
                word.Quit()
            except _ctypes.COMError:
                print("docToPdf: Please close all MS-word processes")
                sys.exit()
        elif self.docFile.lower().endswith(".docx"):
            docx2pdf.convert(self.docFile, "output.pdf")
        else:
            print("Unsupported file format")
            sys.exit(404)

        return outputFile
