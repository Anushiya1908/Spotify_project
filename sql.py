import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import matplotlib.pyplot as plt
import re


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




#track the url we want credentials


track_url = 'https://open.spotify.com/track/7so0lgd0zP2Sbgs2d7a1SZ?si=5b52f6c4ae464b63'

track_id = re.search(r'track/([a-zA-Z0-9]+)',track_url).group(1)

track = sp.track(track_id)

print(track) # print json format details about the song track

track_data = {
    'Track_Name': track['name'],
    'Artist' : track['artists'][0]['name'],
    'Album' : track['album']['name'],
    'Popularity' : track['popularity'],
    'Duration' : track['duration_ms']/60000
}


print(f"\nTrack Name : {track_data['Track_Name']}")
print(f"\nArtist : {track_data['Artist']}")
print(f"\nAlbum : {track_data['Album']}")
print(f"\nPopularity : {track_data['Popularity']}")
print(f"\nDuration : {track_data['Duration']}")

#Convert this into dataframe

df=pd.DataFrame([track_data])
print("\n Track data as data frame: ")
print(df)

#convert to csv

df.to_csv('spotify_track_data.csv',index= False)

#visualize populatity and duration

features = ['Popularity','Duration']

values = [track_data['Popularity'],track_data['Duration']]

plt.figure(figsize=(8,5))
plt.bar(features,values)
plt.title(f"Track data for {track_data['Track_Name']}")
plt.ylabel("values")
plt.show()

