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
username = 'Spotify'

''' 
Writing a loop for extracting data and saving it in a file for every 1000 records
File name = Playlist_{start}_{end}.json 
'''

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





