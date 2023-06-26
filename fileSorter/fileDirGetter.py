import sys
import os
import shutil

TO_READ_PATH = "./toRead"


def getDirs() -> list[str]:
    return [path for path in os.listdir(TO_READ_PATH)
            if (os.path.isdir(os.path.abspath("toRead/" + path)))]


def createCopyInSortedFiles() -> None:
    output: dict = {}
    for directory in getDirs():
        output[directory] = {}
        pathToDirectory: str = TO_READ_PATH + "/" + directory
        # CHECK FOR ZIPS AND UNZIP IT
        for file in os.listdir(pathToDirectory):
            if file.endswith(".zip") or file.endswith(".rar"):
                print("zip found")
                # TODO unzip it
        # SORT BY THICKNESS
        for file in os.listdir(pathToDirectory):
            if file.endswith(".zip") or file.endswith(".rar"):
                continue
            for thickness in range(15, 0, -1):
                thickness = "#" + str(thickness)
                if thickness in file:
                    if thickness not in output[directory]:
                        output[directory][thickness] = []
                    output[directory][thickness].append(file)
                    createCopyOfSortedFile(directory, thickness, file)


def createCopyOfSortedFile(directory, thickness, name):
    if "sortedFiles" not in os.listdir():
        os.mkdir("sortedFiles")
    if directory not in os.listdir("./sortedFiles"):
        os.mkdir("./sortedFiles/" + directory)
    if thickness not in os.listdir("./sortedFiles/" + directory):
        os.mkdir("./sortedFiles/" + directory + "/" + thickness)

    src = os.getcwd() + "/toRead/" + directory + "/" + name
    dst = os.getcwd() + "/sortedFiles/" + directory + "/" + thickness + "/" + name

    shutil.copyfile(src, dst)
