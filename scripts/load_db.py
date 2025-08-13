import pandas as pd
import sqlite3

con = sqlite3.connect('marathon_data.db')
cur = con.cursor()

tcx_df = pd.read_csv('data/data_clean/tcx_clean.csv')
gpx_df = pd.read_csv('data/data_clean/gpx_clean.csv')

tcx_df.to_sql('tcx_data', con, if_exists='replace', index=False)
gpx_df.to_sql('gpx_data', con, if_exists='replace', index=False)

con.commit()
con.close()

