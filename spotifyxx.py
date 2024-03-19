import tkinter as tk
from tkinter import ttk
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from PIL import ImageTk, Image
import os


def get_current_track():
    scope = "user-read-playback-state"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    result = sp.current_playback(market='US', additional_types=('track',))
    if result and result.get('item'):  # Check if there's a current playback and it has an item
        artists = [artist['name'] for artist in result.get('item').get('artists')]
        artist_names = ', '.join(artists)
        track_name = result.get('item').get('name')
        song_info.set(f"{track_name} - {artist_names}")  # Update the label text
    else:
        song_info.set("No track playing")  # Set a default message if nothing is playing
    root.after(5000, get_current_track)  # Refresh every 5000 milliseconds (5 seconds)

root = tk.Tk()
root.title("Spotify Current Track")

song_info = tk.StringVar()
song_info_label = ttk.Label(root, textvariable=song_info, font=('Arial', 20))
song_info_label.pack(pady=20)

get_current_track()  # Initial call to fetch and display the current track

root.mainloop()
