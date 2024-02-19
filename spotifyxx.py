import os 
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError

# username from terminal 
username = sys.argv[1]

# USER ID: 12102296866


try:
    token = util.prompt_for_user_token(username)
except:
    os.remove(f'.cache-{username}')
    token = util.prompt_for_user_token(username)


#spotify object
    
spotifyObject = spotipy.Spotify(auth=token)

