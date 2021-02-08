# %%
import pandas as pd

df = pd.read_csv('crime-housing-austin-2015.csv')
df.head()
df.columns

# %%
seen = []
for index, row in df.iterrows():
    value = row['Highest_NIBRS_UCR_Offense_Description']
    if value not in seen:
        seen.append(value)
print(seen)


# %%
crime = 'Highest_NIBRS_UCR_Offense_Description'
df[df.Highest_NIBRS_UCR_Offense_Description == 'Agg Assault']
# %%
# Graph crimes with x and y coordinates (which are close to transportation?)
# Compare amount of crimes in zip codes with income/race