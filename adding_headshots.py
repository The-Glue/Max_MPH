import pandas as pd
df = pd.read_csv('maxvelo_2025.csv')
base_url = "https://img.mlbstatic.com/mlb-photos/image/upload/w_213,d_people:generic:headshot:silo:current.png,q_auto:best,f_auto/v1/people/{pitcherId}/headshot/67/current"
df['headshotUrl'] = df['pitcherId'].astype(str).apply(lambda x: base_url.format(pitcherId=x))
df.to_csv('maxvelo_2025.csv', index=False)
