import spotipy
from lyricsgenius import Genius
import os
from spotipy.oauth2 import SpotifyOAuth

# Replace with your genius token
genius_token = 'genius token'

# Set environment variable here
os.environ['SPOTIPY_CLIENT_ID'] = 'client id'
os.environ['SPOTIPY_CLIENT_SECRET'] = 'client secret'
os.environ['SPOTIPY_REDIRECT_URI'] ='redirect URI'

scope = 'user-read-currently-playing'

# Get currently playing son from Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
current_song = sp.currently_playing()
artist = current_song['item']['artists'][0]['name']
title = current_song['item']['name']

# Use data from spotify song to find lyrics for the song
genius = Genius(genius_token)

# Display lyrics for the song
song = genius.search_song(title=title, artist=artist)
print(song.lyrics)


