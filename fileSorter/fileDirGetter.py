import sys
import os

TO_READ_PATH = "./toRead"


def getDirs() -> list[str]:
    return [path for path in os.listdir(TO_READ_PATH)
            if (os.path.isdir(os.path.abspath("toRead/" + path)))]



