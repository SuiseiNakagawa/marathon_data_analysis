import pandas as pd
import sqlite3

con = sqlite3.connect('data/marathon_data.db')
cur = con.cursor()

tcx_df = pd.read_csv('data/data_clean/tcx_clean.csv')
official_route_df = pd.read_csv('data/data_clean/official_route.csv')
aid_stations_df = pd.read_csv('data/data_clean/aid_stations.csv')

tcx_df.to_sql('tcx_data', con, if_exists='replace', index=False)
official_route_df.to_sql('official_route_data', con, if_exists='replace', index=False)
aid_stations_df.to_sql('aid_stations_data', con, if_exists='replace', index=False)

con.commit()
con.close()
