import pandas as pd

df = pd.read_csv("data/winemag-data-130k-v2.csv.zip", compression='zip')


group = df[['country', 'points']]

grouped_df = df.groupby('country').agg(
    count=('country', 'size'),        
    points=('points', 'mean')  
).reset_index()

grouped_df.columns = ['country', 'count', 'points']

grouped_df["points"] = grouped_df["points"].round(1)

grouped_df.to_csv("data/reviews-per-country.csv")


