import os

def main():
    data = os.environ["DATA"]

    data = dict((item.split("=") for item in filter(None, data.split("\n"))))

    print(data)

if __name__ == "__main__":
    main()