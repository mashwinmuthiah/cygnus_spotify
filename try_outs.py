import pandas as pd
import spotipy
import oAuth_spotify
from spotipy.oauth2 import SpotifyClientCredentials
import json
import sys
import pickle
import os


with open('playlist_id.txt',"rb") as fp:
    b = pickle.load(fp)
print(len(b))