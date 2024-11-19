# ------------------ MODULES -------------------
"""imported requests module"""
import requests

"""imported BeautifulSoup class from the bs4 module"""
from bs4 import BeautifulSoup

"""imported spotipy module"""
import spotipy
from spotipy.oauth2 import SpotifyOAuth

import os
from dotenv import load_dotenv
load_dotenv()


# ------------------ SCRAPPING THE DATA FROM BILLBOARD -------------------
"""variable to ask and store the date"""
dateInput = input("Which year do you want to travel to? Type the date in this format yyyy-mm-dd: ")

"""variable to store the response"""
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
bbResponse = requests.get(url=f"https://www.billboard.com/charts/hot-100/{dateInput}/", headers=headers)
bbResponse.raise_for_status()

"""variable to store the data"""
bbWebpage = bbResponse.text

"""created soup object"""
soup = BeautifulSoup(bbWebpage, "html.parser")

"""variable to store all the songs details"""
bbSong = soup.find_all(name="h3", id="title-of-a-story")

"""list to store all the songs"""
bbSongs = [song.getText().strip() for song in bbSong]

"""removing unwanted elements"""
unwantedElements = bbSongs[:6]
bbSongs = [element for element in bbSongs if element not in unwantedElements]
bbSongs = [bbSongs[song] for song in range(100)]

# for i in range(len(bbSongs)):
#     print(f"{i + 1}. {bbSongs[i]}")


# ------------------ WORKING WITH SPOTIFY WEB API -------------------

"""variable to store client id"""
spId = os.getenv("SPOTIFY_CLIENT_ID")

"""variable to store client secret"""
spCs = os.getenv("SPOTIFY_CLIENT_SECRET")

"""authentication with spotify"""
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=spId,
        client_secret=spCs,
        show_dialog=True,
        cache_path="token.txt"
    )
)

"""searching spotify for the songs"""
user_id = sp.current_user()["id"]

song_uris = []
year = dateInput.split("-")[0]
for song in bbSongs:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

"""Creating a new private playlist in Spotify"""
playlist = sp.user_playlist_create(user=user_id, name=f"{dateInput} Billboard 100", public=False)
# print(playlist)

"""Adding songs found into the new playlist"""
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

