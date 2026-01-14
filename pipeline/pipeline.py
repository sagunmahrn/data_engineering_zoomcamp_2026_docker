import sys
import pandas as pd
print("arguments", sys.argv)

month = int(sys.argv[1])

# df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
df = pd.DataFrame({"day":[1,2],"num_passengers":[3,4]})
df['month'] = month
print(df.head())

# df.to_parquet(f"output_day_{sys.argv[1]}.parquet")
df.to_parquet(f"output_{month}.parquet")
print(f"Running pipeline for month {month}")
