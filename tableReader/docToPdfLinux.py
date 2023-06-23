import subprocess
import sys
import os


class DocToPDF:
    """Converts .doc and .docx files to pdf"""

    def __init__(self, docFile):
        self.docFile: str = docFile.replace("\\", "/")

    def convertToPDF(self) -> str:
        """Convert file to pdf. returns name of file"""

        outputFile = "./tableReader"
        # print(os.path.abspath(self.docFile).replace("\\","/"))
        cmd = 'libreoffice --headless --convert-to pdf'.split() + [self.docFile, "--outdir",
                                                                   outputFile]
        p = subprocess.Popen(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        p.wait(timeout=10)
        stdout, stderr = p.communicate()
        if stderr:
            raise subprocess.SubprocessError(stderr)
        tempName: str = outputFile + "/" + self.docFile.split("/")[-1].replace(".doc", ".pdf")
        outputFile = outputFile + "/temp.pdf"
        os.rename(tempName, outputFile)

        return outputFile
