from tcxreader.tcxreader import TCXReader
import pandas as pd

# convert TCX to DataFrame
tcx_reader = TCXReader()
tcx_data = tcx_reader.read('data_raw/San_Francisco_Marathon.tcx')

rows = []
for lap in tcx_data.laps:
    for trackpoint in lap.trackpoints:
        rows.append({
            'time': trackpoint.time,
            'latitude': trackpoint.latitude,
            'longitude': trackpoint.longitude,
            'elevation': trackpoint.elevation,
            'distance': trackpoint.distance,
            'heart_rate': trackpoint.hr_value
        })

tcx_df = pd.DataFrame(rows)

# save to CSV
tcx_df.to_csv('data_clean/tcx_clean.csv', index=False)
