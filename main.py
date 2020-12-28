import spotipy
from lyricsgenius import Genius
from spotipy.oauth2 import SpotifyOAuth
import PySimpleGUI as sg

# Replace with your genius token
genius_token = 'rPDC-micVZJUPXkpTWFSxWhcCOUR0jQPJAd8L6-VeFF-FzXgk0sTvl9fOvpiXyHl'

# Get currently playing song from Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="ca70883df7f3499aa26bf8d0b195f4be",
                                               client_secret="290d2192ab7a4b2699a731b16aa71bea",
                                               redirect_uri="http://example.com",
                                               scope="user-read-currently-playing"))


# Use data from spotify song to find lyrics for the song
genius = Genius(genius_token)

# Set up popup window
sg.theme('Dark')
layout = [[sg.Text('Press button to find lyrics to your song', key='-TOP-', size=(50, 1))],
          [sg.Multiline('No lyrics available', key='-SONG-', size=(100,50))],
          [sg.Button('Find Song'), sg.Button('Quit')]]
window = sg.Window('Song Lyrics', layout)

# Create event to get lyrics after pressing 'Find Song' button
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    elif event == 'Find Song':
        # Display song lyrics
        current_song = sp.currently_playing()
        artist = current_song['item']['artists'][0]['name']
        title = current_song['item']['name']
        window['-TOP-'].update(genius.search_song(title=title, artist=artist))
        window['-SONG-'].update(genius.search_song(title=title, artist=artist).lyrics)
window.close()
