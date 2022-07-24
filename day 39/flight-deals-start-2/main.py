# # This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# # program requirements.
from flight_data import FlightSearch

import requests


search = FlightSearch()
url = "https://api.sheety.co/1f962c422a996366521f1b89ef60bb06/flightDeals/prices/"
res = requests.get(url)
sheet_data = res.json()
destination_data = sheet_data["prices"]


if destination_data[0]['iataCode'] == '':
    for row in destination_data:
        row['iataCode'] = search.get_destination_code(row["city"])
    print(destination_data)

def iata_codes():
    for city in destination_data:
        new_data = {
            'price': {
                'iataCode': city['iataCode']
            }
        }

        response = requests.put(url=f"{url}/{city['id']}", json=new_data)
        print(response.text)
    return response
# #
# iata_codes()