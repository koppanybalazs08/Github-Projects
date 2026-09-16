import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

data = pd.read_csv("dataset.csv")

fig, axes = plt.subplots(2,2,figsize = (11,8))

artists = data["artists"].unique()
tracks = []
artists_occur_series = data["artists"].value_counts()

for artist in artists:
    tracks.append(artists_occur_series.get(artist))

artists_occur_dt = pd.DataFrame({"track_count" : tracks, "artist" : artists}).dropna().sort_values(by = "track_count", ascending = False)
top_5_artists = artists_occur_dt.iloc[0:5]

track_counts = [
                len(artists_occur_dt.loc[artists_occur_dt["track_count"] >= 100]),
                len(artists_occur_dt.loc[(artists_occur_dt["track_count"] >= 50) & (artists_occur_dt["track_count"] < 100)]),
                len(artists_occur_dt.loc[(artists_occur_dt["track_count"] >= 20) & (artists_occur_dt["track_count"] < 50)])
                ]
track_counts_dt = pd.DataFrame({"no_of_artists" : track_counts, "category" : ["more than 100", "more than 50", "more than 20"]})

popularity_duration = data.loc[:, ["popularity"]]
duration = data.loc[:, ["duration_ms"]].div(1000)

popularity_duration["duration_s"] = duration["duration_ms"]
popularity_duration.dropna().sort_values(by = "popularity", ascending = False)
popularity_duration = popularity_duration[popularity_duration["duration_s"] <= np.percentile(popularity_duration["duration_s"],99.9)]

explode = [0.1, 0.1, 0.1]
piechart = axes[0][0].pie(track_counts_dt["no_of_artists"], shadow = True, explode = explode, startangle = 30)
axes[0][0].pie_label(piechart, track_counts_dt["category"], distance = 1.1)
axes[0][0].pie_label(piechart, '{frac:.1%}', distance = 0.8)
axes[0][0].set_title("Percentage of artists with more than x tracks")

barplot = sns.barplot(ax = axes[0][1], data = top_5_artists, y = "track_count", x = "artist", color = "#FFC832")
barplot.set(xlabel = "", title = "top 5 artists & the number of track they have")
barplot.set_xticks(top_5_artists["artist"], labels = top_5_artists["artist"], rotation = 15)

scatterplot = sns.scatterplot(ax = axes[1][0], data = popularity_duration, x = "duration_s", y = "popularity", s = 15)
scatterplot.set(xlabel = "duration in seconds", title = "popularity vs track length")

plt.show()