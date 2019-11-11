import pandas as pd
import spotipy
import oAuth_spotify
from spotipy.oauth2 import SpotifyClientCredentials
import json
import os
import sys
import pickle

# Authorizing with spotify API credentials
# Client_ID and Client_Secret = "Get-your-client-id-from-spotify-developer-website" 
client_credentials_manager = SpotifyClientCredentials(oAuth_spotify.Client_ID,oAuth_spotify.Client_Secret)

#Creating a Spotipy object, we use this to get all the data we need
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

#We are collecting Data about the playlists created by Spotify itself
username = 'Spotify'


def make_playlist_list(start,end):
    if os.path.exists('playlist_id.txt'):
        with open("playlist_id.txt", "rb") as fp: 
            old_data = pickle.load(fp)
    else : old_data = []

    lst = old_data

    for i in range(start, end, 50):
        a = sp.user_playlists("Spotify", limit=50, offset=i)
        playlist_id = (a['items'])
        for j in range(0,len(playlist_id)):
            x = playlist_id[j]['id']
            print(x)
            lst.append(x)
    with open("playlist_id.txt", "wb") as fp:   #Pickling
        pickle.dump(lst, fp)
    
    print('Number of Playlists id extracted :',len(lst))
    del lst


start = 0
end = 2000
make_playlist_list(start,end)        

def track_ids():
    with open("playlist_id.txt", "rb") as fp:   # Unpickling and getting the List of Playlist id's
        b = pickle.load(fp)
    tracks_id = []
    for progress,i in enumerate(b):
        tracks = sp.user_playlist_tracks(username, playlist_id=i, limit=100)

        for item in tracks['items']:
                if item['track'] is not None:
                    tracks_id.append(item['track']['id'])
                else :
                    print('Not Found in {}'.format(progress))
    print('Number of Track Id Extracted {}'.format(len(tracks_id)))

    with open('track_id.txt',"wb") as fp:
        pickle.dump(tracks_id,fp)
    del tracks_id,b

track_ids()


def get_songs_details():

    with open('track_id.txt',"rb") as fp:
        b = pickle.load(fp)
    print('Number of unique Songs id extracted : ',len(set(b)))

get_songs_details()


