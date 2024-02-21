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
print(result.get('item').get('album').get('name'))
artists = [artist['name'] for artist in result.get('item').get('artists')]
artist_names = ', '.join(artists)
print(result.get('item').get('name'), '-', artist_names)
