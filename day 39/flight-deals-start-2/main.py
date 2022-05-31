# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.

import requests
from pprint import pprint
url = "https://api.sheety.co/1f962c422a996366521f1b89ef60bb06/flightDeals/prices"
put_url = "https://api.sheety.co/1f962c422a996366521f1b89ef60bb06/flightDeals/prices"
res = requests.get(url)
sheet_data = res.json()
destination_data = sheet_data["prices"]

def iata_codes():

    sheet = [sheet["iataCode"] for sheet in destination_data]
    if len(sheet) == "":
        for city in destination_data:
            new_data = {
                    "prices": {
                        "iataCode": "TESTING"
                    }
                }
        response = requests.put(url=f"{put_url}/{city['id']}", json=new_data)


        print(response.text())
#
print(iata_codes())