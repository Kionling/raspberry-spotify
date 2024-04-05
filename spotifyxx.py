import io
import urllib.request
from PIL import Image, ImageTk
import tkinter as tk
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time
from weather import getweather, getDescription
import asyncio

def update_time():
    current_time = time.strftime("%I:%M:%S")
    time_label.config(text=current_time)
    root.after(1000, update_time)  # Call this function again in 1000 milliseconds (1 second)

def get_current_track():
    scope = "user-read-playback-state"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    result = sp.current_playback(market='US', additional_types=('track',))
    if result and result.get('item'):  # Check if there's a current playback and it has an item
        artists = [artist['name'] for artist in result.get('item').get('artists')]
        artist_names = ', '.join(artists)
        track_name = result.get('item').get('name')
        song_info.set(f"{track_name} - {artist_names}")  # Update the label text
        
        # Fetch album art
        album_art_url = result.get('item').get('album').get('images')[0].get('url')
        image_bytes = urllib.request.urlopen(album_art_url).read()
        # Open image and convert to PhotoImage
        data_stream = io.BytesIO(image_bytes)
        pil_image = Image.open(data_stream)
        tk_image = ImageTk.PhotoImage(pil_image)
        album_art_label.configure(image=tk_image)
        album_art_label.image = tk_image  # Keep a reference!
    else:
        song_info.set("No track playing")  # Set a default message if nothing is playing
    
    root.after(5000, get_current_track)  # Refresh every 5000 milliseconds (5 seconds)

weather = asyncio.run(getweather())
description = asyncio.run(getDescription())

root = tk.Tk()
root.title("Spotify Current Track")
root.minsize(1620, 780)
dark_background = "#121212"
light_text = "#E0E0E0"
root.configure(bg=dark_background)

# Configure grid layout with flexible rows for vertical centering
root.grid_rowconfigure(0, weight=1)  # Flexible space before labels
root.grid_rowconfigure(1, weight=0)  # Minimal space, adjust if needed
root.grid_rowconfigure(2, weight=0)  # Minimal space, adjust if needed
root.grid_rowconfigure(3, weight=1)  # Flexible space after labels
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
# weather label 
weather_label = tk.Label(root, text=weather, font=('Arial', 20), bg=dark_background, fg=light_text)
weather_label.grid(row=3, column=0, sticky="ew", padx=20)
# Time label centered vertically
time_label = tk.Label(root, font=('Arial bold', 100), bg=dark_background, fg=light_text)
time_label.grid(row=1, column=0, sticky="ew", padx=20)
update_time()  # Initial call to start updating the time

# Song info label centered vertically
song_info = tk.StringVar()
song_info_label = tk.Label(root, textvariable=song_info, font=('Arial', 20), bg=dark_background, fg=light_text)
song_info_label.grid(row=2, column=0, sticky="ew", padx=20)

# Album art label
album_art_label = tk.Label(root, bg=dark_background)
album_art_label.grid(row=0, column=1, rowspan=4, sticky="nesw", padx=20, pady=20)

get_current_track()  # Initial call to fetch and display the current track

root.mainloop()
