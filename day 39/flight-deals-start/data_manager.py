import requests
import os


FLIGHT_DATA_ENPOINT = os.environ['FLIGHT_DATA']



class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.flight_data = {}

    def get_flight_data(self):
        response = requests.get(FLIGHT_DATA_ENPOINT)
        json = response.json()
        self.destination_data = json["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
        response = requests.put(
            url=f"{FLIGHT_DATA_ENPOINT}/{city['id']}",
            json= new_data
        )
        print(response.text)


