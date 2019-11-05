import pandas as pd
import spotipy
import oAuth_spotify
from spotipy.oauth2 import SpotifyClientCredentials
import os
import json
from json.decoder import JSONDecodeError
import sys

client_credentials_manager = SpotifyClientCredentials(oAuth_spotify.Client_ID,oAuth_spotify.Client_Secret)

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

username = 'Spotify'

'''playlists = sp.user_playlists(username,limit = 1)
a = json.dumps(playlists['items'],indent=4)
print(a)'''

end = 1000
start = 0
total = 10000
while end <= total:

    for offs in range(start,end,50):
        if offs == start:
            playlists = sp.user_playlists(username,limit = 50)
            a = json.dumps(playlists['items'],indent=4)
        else:   
            playlists = sp.user_playlists(username,offset = offs,limit = 1)
            a = a + json.dumps(playlists['items'],indent=4)

    file_name = 'playlist'+'_'+str(start)+'_'+str(end-1)+'.json'

    with open(file_name,'w') as f:
        f.write(a.replace('][',','))
    
    bar_len = 100
    perc = int(end/total*100)
    bar = "="*perc + '-'*(bar_len-perc)
    sys.stdout.write("[%s] %d%% \r" % (bar,perc))
    sys.stdout.flush()

    end = end + 1000
    start = start + 1000

print('------END------')





