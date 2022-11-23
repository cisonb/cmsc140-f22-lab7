import pandas as pd
import os.path

file = pd.read_csv(r"C: /Users/brycecison/cmsc140-f22-lab7-1/city_temperature.csv", mar = ",")

group = file.loc[file.groupby(['Region'])['AvgTemperature'].idxmax()]

print(group)

group.to_csv(os.path.join(r"C: /Users/brycecison/cmsc140-f22-lab7-1/city_temperature.csv", 'city_maxtemp.csv'))