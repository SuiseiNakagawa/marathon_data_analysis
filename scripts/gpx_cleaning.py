import gpxpy
import pandas as pd

with open('data/data_raw/San_Francisco_Marathon.gpx', 'r') as gpx_file:
    gpx = gpxpy.parse(gpx_file)

# convert GPX to DataFrame
gpx_data = []
for track in gpx.tracks:
    for segment in track.segments:
        for point in segment.points:
            gpx_data.append({
                'latitude': point.latitude,
                'longitude': point.longitude,
                'elevation': point.elevation,
                'time': point.time
            })

gpx_df = pd.DataFrame(gpx_data)

# save to CSV
gpx_df.to_csv('data_clean/gpx_clean.csv', index=False)
