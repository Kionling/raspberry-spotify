import io
import urllib.request
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
import spotipy
from spotipy.oauth2 import SpotifyOAuth

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

root = tk.Tk()
root.title("Spotify Current Track")
dark_background = "#121212"
light_text = "#E0E0E0"
root.configure(bg=dark_background)

# Song info label
song_info = tk.StringVar()
song_info_label = ttk.Label(root, textvariable=song_info, font=('Arial', 20))
song_info_label.pack(pady=20)
# Album art label
album_art_label = tk.Label(root)
album_art_label.pack(pady=20)

get_current_track()  # Initial call to fetch and display the current track

root.mainloop()
