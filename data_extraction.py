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
Getting Playlist Details

Writing a function for extracting data and saving it in a file for every 1000 records
File name = Playlist_{start}_{end}.json 
'''

def get_playlists(start,end,total):
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

    print('\n ------END------')

# Call the function with the start,end and Total records needed.

end = 21000
start = 20000
total = 30000

## get_playlists(start,end,total)

''' Making a list of playlists ID '''

def make_playlist_list(start,end):
    P_list = []
    while end<=30000:
        print(start,end)
        url = r'C:\Users\ashwi\Desktop\Ashwin\cygnus_spotify\Data\playlist_'+str(start)+'_'+str(end-1)+'.json'
        with open(url) as f:
            data = json.load(f)
            for j in data:
                P_list.append(j['id'])

        start = start + 1000
        end = end + 1000

    print(len(P_list))

    return P_list

start = 0
end = 1000
P_list = make_playlist_list(start,end)        

''' Getting the songs using the P_list and the API '''









