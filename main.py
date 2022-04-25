from src.apiextractor import APIExtractor
from src.uploadstorage import WriteToCloud


def main():
    x = APIExtractor("ce", "caucaia")

    x.return_json()


if __name__ == "__main__":
    main()
