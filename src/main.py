import json
import urllib.request


def main():
    with urllib.request.urlopen("https://api.bitflyer.com/v1/ticker") as resp:
        data = json.load(resp)
    print(data)


if __name__ == "__main__":
    main()
