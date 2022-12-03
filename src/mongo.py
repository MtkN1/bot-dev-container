import json
import urllib.request

import pymongo


def main():
    with urllib.request.urlopen("https://api.bitflyer.com/v1/ticker") as resp:
        data = json.load(resp)

    mongo = pymongo.MongoClient()
    print("Inserting data ...")
    mongo.test.bitflyer.insert_one(data)
    document = mongo.test.bitflyer.find_one()
    print(f"Fetched data: {document}")


if __name__ == "__main__":
    main()
