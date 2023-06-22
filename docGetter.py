import os
import sys


def getFiles() -> list:
    """Returns list of files from toRead directory."""
    # Check if there are doc / docx files are in directory
    readDir = "toRead"
    listOfFiles = os.listdir(readDir)
    listOfFiles = [fileName for fileName in listOfFiles
                   if fileName.lower().endswith(".docx")
                   or fileName.lower().endswith(".doc")]
    # Extract files from order directories
    if len(listOfFiles) == 0:
        for file in os.listdir(readDir):
            d = os.path.join(readDir, file)
            if os.path.isdir(d):
                for fileName in os.listdir(d):
                    if fileName.lower().endswith(".docx") or \
                            fileName.lower().endswith(".doc"):

                        listOfFiles.append(
                            (d + "\\" + fileName).replace(readDir, "")
                        )

    return listOfFiles


class DocGetter:
    pass
