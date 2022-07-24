import requests


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.headers = {
            "apikey": '9GrzY_rQNQJok1fnD0TKM9oOBFZ2sYi0'
        }

    def get_destination_code(self, city_name: str):
        url = f'https://tequila-api.kiwi.com/locations/query?term={city_name}&locale=en-US&location_types=airport&' \
              f'limit=10&active_only=true'
        res = requests.get(url, headers=self.headers)
        response_text = res.json()['locations']
        city_code = response_text[0]['city']['code']

        return city_code




