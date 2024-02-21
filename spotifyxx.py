import os 
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError
from spotipy.oauth2 import SpotifyOAuth

scope = "user-read-playback-state"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

result = sp.current_playback(market='US', additional_types=('track'))

# print(result.get('item').get('name'))
# print(result.get('item').get('name'), '-', result.get('item').get('artists')[0].get('name'))


# Iterate through the list of artists and print their names
for artist in result.get('item').get('artists'):
    print(artist['name'])


# print(json.dumps(result.get('item').get('artists'), sort_keys=True, indent=4))

