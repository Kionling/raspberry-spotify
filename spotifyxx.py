import os 
import sys 
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth
import tkinter as tk
from tkinter import ttk

def get_current_track():
    scope = "user-read-playback-state"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    result = sp.current_playback(market='US', additional_types=('track'))
    artists = [artist['name'] for artist in result.get('item').get('artists')]
    artist_names = ', '.join(artists)
    print(result.get('item').get('name'), '-', artist_names)

root = tk.Tk()
root.title("Spotify Current Track")
song_info = tk.StringVar()
song_info_label = ttk.Label(root, textvariable=song_info, font=('Arial', 20))
song_info_label.pack(pady=20)


get_current_track()
    
root.mainloop()