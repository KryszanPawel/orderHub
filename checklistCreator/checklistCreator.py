from outputScanner import OutputScanner

PATH_TO_OUTPUT = "output.xlsx"

if __name__ == "__main__":

    data = OutputScanner(PATH_TO_OUTPUT).getData()

    for index, row in data.iterrows():
        print(row)
        print()

