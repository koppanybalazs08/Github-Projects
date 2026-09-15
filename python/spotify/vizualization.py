import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("dataset.csv")

fig, axes = plt.subplots(2,2,figsize = (11,8))

artists = data["artists"].unique()
tracks = []
artists_occur_series = data["artists"].value_counts()

for artist in artists:
    tracks.append(artists_occur_series.get(artist))

artists_occur_dt = pd.DataFrame({"track_count" : tracks, "artist" : artists}).dropna()
track_counts = [
                len(artists_occur_dt.loc[artists_occur_dt["track_count"] >= 100]),
                len(artists_occur_dt.loc[(artists_occur_dt["track_count"] >= 50) & (artists_occur_dt["track_count"] < 100)]),
                len(artists_occur_dt.loc[(artists_occur_dt["track_count"] >= 20) & (artists_occur_dt["track_count"] < 50)])
                ]
track_counts_dt = pd.DataFrame({"no_of_artists" : track_counts, "category" : ["more than 100", "more than 50", "more than 20"]})
explode = [0.1, 0.1, 0.1]


axes[0][0].pie(track_counts_dt["no_of_artists"], labels = track_counts_dt["category"], shadow = True, explode = explode)

plt.show()