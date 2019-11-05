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
username = 'spotify'
playlists = sp.user_playlists(username,limit = 3)


print(json.dumps(playlists,indent=4))

print('------END------')




