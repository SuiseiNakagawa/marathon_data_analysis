import gpxpy
import pandas as pd

with open('data/data_raw/San_Francisco_Marathon.gpx', 'r') as gpx_file:
    gpx = gpxpy.parse(gpx_file)

# Process my race GPX data
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
gpx_df.to_csv('data/data_clean/gpx_clean.csv', index=False)
print(f"Saved {len(gpx_data)} GPX points")

# Process official route GPX
with open('data/data_raw/official_SFM_route.gpx', 'r') as gpx_file:
    gpx = gpxpy.parse(gpx_file)

route_data = []
for track in gpx.tracks:
    for segment in track.segments:
        for point in segment.points:
            route_data.append({
                'latitude': point.latitude,
                'longitude': point.longitude,
                'elevation': point.elevation,
            })

route_df = pd.DataFrame(route_data)
route_df.to_csv('data/data_clean/official_route.csv', index=False)
print(f"Saved {len(route_data)} route points")

# Process aid stations
waypoints = []
for waypoint in gpx.waypoints:
    waypoints.append({
        'name': waypoint.name,
        'latitude': waypoint.latitude,
        'longitude': waypoint.longitude,
        'type': waypoint.type
    })

if waypoints:
    waypoints_df = pd.DataFrame(waypoints)
    waypoints_df.to_csv('data/data_clean/aid_stations.csv', index=False)
    print(f"Saved {len(waypoints)} aid stations")