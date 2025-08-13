import gpxpy
import pandas as pd

with open('data_raw/San_Francisco_Marathon.gpx', 'r') as gpx_file:
    gpx = gpxpy.parse(gpx_file)

# convert GPX to DataFrame
route_info = []
for track in gpx.tracks:
    for segment in track.segments:
        for point in segment.points:
            route_info.append({
                'latitude': point.latitude,
                'longitude': point.longitude,
                'elevation': point.elevation,
                'time': point.time
            })

route_df = pd.DataFrame(route_info)

# save to CSV
route_df.to_csv('data_clean/gpx_clean.csv', index=False)
