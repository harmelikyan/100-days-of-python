from unittest import result

from bs4 import BeautifulSoup
import requests

import spotipy
from spotipy.oauth2 import SpotifyOAuth

spotify_id = ''
spotify_secret = ''



sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope="playlist-modify-private playlist-read-private",
    redirect_uri="http://example.com",
    client_id=spotify_id,
    client_secret=spotify_secret,
    show_dialog=True,
    cache_path="/Users/harmelikyan/Desktop/Programming/app_brewery/gith/100_days_of_python/day 46/token.txt"
    ))

user_id = sp.current_user()["id"]
print(user_id)

date_input = input("Which year do you want to travel to? Enter a date in format YYYY-MM-DD\n")
response = requests.get(f"https://www.billboard.com/charts/hot-100/{date_input}")
response_text = response.text

soup = BeautifulSoup(response_text, 'html.parser')
find_title = soup.find_all(name='h3', class_='a-no-trucate')
list_of_titles = [title.getText().strip() for title in find_title]

song_uris = []
year = date_input.split('-')[0]
for song in list_of_titles:
    result = sp.search(q=f'track:{song} year:{year}', type='track')
    # print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{date_input} Billboard 100", public=False)
print(playlist)
# print(list_of_titles)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

