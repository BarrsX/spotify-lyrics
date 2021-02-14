import spotipy
from lyricsgenius import Genius
from spotipy.oauth2 import SpotifyOAuth
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def index():
    # Replace with your genius token
    genius_token = 'rPDC-micVZJUPXkpTWFSxWhcCOUR0jQPJAd8L6-VeFF-FzXgk0sTvl9fOvpiXyHl'

    # Get currently playing song from Spotify
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="ca70883df7f3499aa26bf8d0b195f4be",
                                                   client_secret="290d2192ab7a4b2699a731b16aa71bea",
                                                   redirect_uri="http://example.com",
                                                   scope="user-read-currently-playing"))

    # Use data from spotify song to find lyrics for the song
    genius = Genius(genius_token)
    current_song = sp.currently_playing()
    artist = current_song['item']['artists'][0]['name']
    title = current_song['item']['name']
    song = genius.search_song(title=title, artist=artist)
    lyrics = genius.search_song(title=title, artist=artist).lyrics
    lyrics = lyrics.split('\n')
    return render_template('index.html', lyrics=lyrics, song=song)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
