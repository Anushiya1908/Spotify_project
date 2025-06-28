import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import matplotlib.pyplot as plt
import re
import mysql.connector


#Client credentials
sp = spotipy.Spotify(auth_manager= SpotifyClientCredentials(
    client_id='ec2e32163edc4007a6022ffaee3c0bb6',
    client_secret='ae3d12493bcd4aa68788552d5c9a2a2d'
))

#configuration

df_config = {'host' : 'localhost',
'user' : 'root',
'password' : 'root',
'database' : 'spotify_df'
}

connection = mysql.connector.connect(**df_config)
cursor = connection.cursor()



#track the url we want credentials


track_url = 'https://open.spotify.com/track/7so0lgd0zP2Sbgs2d7a1SZ?si=5b52f6c4ae464b63'

track_id = re.search(r'track/([a-zA-Z0-9]+)',track_url).group(1)

track = sp.track(track_id)

print(track) # print json format details about the song track

track_data = {
    'Track_Name': track['name'],
    'Artists' : track['artists'][0]['name'],
    'Album' : track['album']['name'],
    'Popularity' : track['popularity'],
    'Duration' : track['duration_ms']/60000
}

#insert sql query

insert_data = """
INSERT into spotify_tracks(Track_Name,Artists,Album,Popularity,Duration)
VALUES (%s,%s,%s,%s,%s)
"""

cursor.execute(insert_data,(
    track_data['Track_Name'],
    track_data['Artists'],
    track_data['Album'],
    track_data['Popularity'],
    track_data['Duration']
))

connection.commit()

print(f"\n Track data for {track_data['Track_Name']} inserted into the database")

cursor.close()
connection.close()