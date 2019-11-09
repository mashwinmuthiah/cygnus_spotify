import pandas as pd
import spotipy
import oAuth_spotify
from spotipy.oauth2 import SpotifyClientCredentials
import json
import sys

# Authorizing with spotify API credentials
# Client_ID and Client_Secret = "Get-your-client-id-from-spotify-developer-website"
client_credentials_manager = SpotifyClientCredentials(oAuth_spotify.Client_ID,oAuth_spotify.Client_Secret)

#Creating a Spotipy object, we use this to get all the data we need
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

#We are collecting Data about the playlists created by Spotify itself
username = 'ashwinmuthiah'
pl_id = '3ViIr5ew8RXOgyNkdRS9V4'

''' 
Writing a function for extracting data and saving it in a file for every 1000 records
File name = Playlist_{start}_{end}.json 
'''
tracks = sp.user_playlist_tracks(user = username , playlist_id= pl_id,limit=2)['items']
with open('song_try.json','w') as f:
    json.dump(tracks,f,indent=4)

print('-------END------')



