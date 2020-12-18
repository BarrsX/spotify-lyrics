import spotipy
from lyricsgenius import Genius
from spotipy.oauth2 import SpotifyOAuth

# Replace with your genius token
genius_token = 'genius_token'

# Get currently playing song from Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="client_id",
                                               client_secret="client_secret",
                                               redirect_uri="redirect_uri",
                                               scope="scope"))
current_song = sp.currently_playing()
artist = current_song['item']['artists'][0]['name']
title = current_song['item']['name']

# Use data from spotify song to find lyrics for the song
genius = Genius(genius_token)

# Display lyrics for the song
song = genius.search_song(title=title, artist=artist)
print(song.lyrics)
