import pandas as pd
import oAuth_spotify
import json
import sys
import pickle
import os
import requests

grant_type = 'client_credentials'
body_params = {'grant_type' : grant_type}
url='https://accounts.spotify.com/api/token'
response = requests.post(url, data=body_params, auth = (oAuth_spotify.Client_ID,oAuth_spotify.Client_Secret)) 
token_raw = json.loads(response.text)
token = token_raw["access_token"]

headers = {"Authorization": "Bearer {}".format(token)}
url="https://api.spotify.com/v1/users/ashwinmuthiah/playlists"
r = requests.get(url, headers=headers)
print(r.text)