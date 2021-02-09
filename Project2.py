# %%
import pandas as pd
import seaborn as sns

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
# Graph crimes with x and y coordinates (which are close to transportation?)
# Compare amount of crimes in zip codes with income/race
# %%
sns.scatterplot(x=agg.X_Coordinate, y=agg.Y_Coordinate)
# %%
from scipy.stats import ttest_ind

crime = 'Highest_NIBRS_UCR_Offense_Description'
df[df.Highest_NIBRS_UCR_Offense_Description == 'Agg Assault']
agg = df[df.Highest_NIBRS_UCR_Offense_Description == 'Agg Assault']

agg['Medianhouseholdincome'] = agg['Medianhouseholdincome'].str.replace('$', '').astype('float')
zip_codes = agg.groupby(by=['Zip_Code_Crime']).agg({'Medianhouseholdincome': 'mean', 'Key': 'count'}).reset_index().dropna()
sns.scatterplot(x=zip_codes['Medianhouseholdincome'], y=zip_codes['Key'])
# %%
from scipy.stats import ttest_ind
from sklearn import preprocessing

names = zip_codes.columns
scaler = preprocessing.StandardScaler()
scaled_df = scaler.fit_transform(zip_codes)
scaled_df = pd.DataFrame(scaled_df, columns=names)


sns.distplot(scaled_df['Medianhouseholdincome'], label='Median Household Income', hist=False)
sns.distplot(scaled_df['Key'], label='Number of aggravated assaults', hist=False)
ttest_ind(scaled_df['Medianhouseholdincome'], scaled_df['Key'])
# %%
