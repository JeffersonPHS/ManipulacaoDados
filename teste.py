import json


def readJson():
    try:
        with open("instituicoes.json", "r") as file:
            data = json.load(file)

        print("File data =", data)

    except FileNotFoundError:
        print("Error: 'data.json' file was not found.")


def main(args=[]):
    readJson()


if __name__ == "__main__":
    main()
