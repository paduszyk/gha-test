import os

def main():
    data = os.environ["DATA"]

    data = dict((item.split("=") for item in data.split("\n")))

    print(data)

if __name__ == "__main__":
    main()