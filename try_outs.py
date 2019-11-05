import pandas as pd
import spotipy
import oAuth_spotify
from spotipy.oauth2 import SpotifyClientCredentials
import os
import json
from json.decoder import JSONDecodeError
import spotipy.util as util

client_credentials_manager = SpotifyClientCredentials(oAuth_spotify.Client_ID,oAuth_spotify.Client_Secret)

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
username = 'Spotify'

playlists = sp.user_playlists(username)

'''for offs in range(0,101,50):
    playlists = sp.user_playlists(username,offset = offs,limit = 50)
    print(json.dumps(playlists,indent=4))
'''

for offs in range(0,501,50):
    with open('playlist.json','a+') as f:
        playlists = sp.user_playlists(username,offset = offs,limit = 50)
        json.dump(playlists['items'],f,indent=4,sort_keys=True)
        

print('------END------')




