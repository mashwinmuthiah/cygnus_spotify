import pandas as pd
import spotipy
import oAuth_spotify
from spotipy.oauth2 import SpotifyClientCredentials
import json
import sys
import pickle


# Authorizing with spotify API credentials
# Client_ID and Client_Secret = "Get-your-client-id-from-spotify-developer-website" 
client_credentials_manager = SpotifyClientCredentials(oAuth_spotify.Client_ID,oAuth_spotify.Client_Secret)

#Creating a Spotipy object, we use this to get all the data we need
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

#We are collecting Data about the playlists created by Spotify itself
username = 'Spotify'


with open("playlist_id.txt", "rb") as fp:   # Unpickling and getting the List of Playlist id's
    b = pickle.load(fp)

tracks_id = []
tracks = sp.user_playlist_tracks(username, playlist_id=b[1], limit=100)
a = json.dumps(tracks,indent=4)

for i,item in enumerate(tracks['items']):
    
    if item['track'] is not None:
        print(i)
        ## print(item['track']['id'])
    else:
        print('Not there')

print(tracks_id)
