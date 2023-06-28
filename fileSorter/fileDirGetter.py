import sys
import os
import shutil
import zipfile

TO_READ_PATH = "./toRead"


def getDirs() -> list[str]:
    return [path for path in os.listdir(TO_READ_PATH)
            if (os.path.isdir(os.path.abspath("toRead/" + path)))]


def createCopyInSortedFiles() -> None:
    """Create copy of order file sorted way"""
    clearSortedFiles()
    for directory in getDirs():
        pathToDirectory: str = TO_READ_PATH + "/" + directory
        # CHECK FOR ZIPS AND UNZIP IT
        for file in os.listdir(pathToDirectory):
            if file.endswith(".zip") or file.endswith(".rar"):
                print("Unzipping: " + pathToDirectory + "/" + file)
                with zipfile.ZipFile(pathToDirectory + "/" + file) as zipFile:
                    zipFile.extractall(pathToDirectory)
        # SORT BY THICKNESS
        for file in os.listdir(pathToDirectory):
            if file.endswith(".zip") or file.endswith(".rar"):
                continue
            for thickness in range(15, 0, -1):
                thickness = "#" + str(thickness)
                if thickness in file:
                    createCopyOfSortedFile(directory, thickness, file)
                    break
    renameSortedDirectories()


def createCopyOfSortedFile(directory, thickness, name):
    if "sortedFiles" not in os.listdir():
        os.mkdir("sortedFiles")
    if directory not in os.listdir("./sortedFiles"):
        os.mkdir("./sortedFiles/" + directory)
    if thickness not in os.listdir("./sortedFiles/" + directory):
        os.mkdir("./sortedFiles/" + directory + "/" + thickness)

    src = os.getcwd() + "/toRead/" + directory + "/" + name
    dst = os.getcwd() + \
          "/sortedFiles/" + directory + "/" + thickness + "/" + name

    shutil.copyfile(src, dst)


def renameSortedDirectories():
    for directory in os.listdir("./sortedFiles"):
        newName = [directory]
        for thickness in os.listdir("./sortedFiles/" + directory):
            newName.append(thickness)

        thicknessToSort = sorted([int(item.replace("#","")) for item in newName[1:]])
        newName = newName[0:1] + ["#" + str(item) for item in thicknessToSort]

        os.rename("./sortedFiles/" + directory,
                  "./sortedFiles/" + "_".join(newName))

def clearSortedFiles():
    if "sortedFiles" in os.listdir():
        shutil.rmtree("./sortedFiles", ignore_errors=True)

