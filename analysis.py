import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('Western_Leopard_Toad.csv')


df['observed_on'] = pd.to_datetime(df['observed_on'])

df['year'] = df['observed_on'].dt.year
df['month'] = df['observed_on'].dt.month


plt.figure(figsize=(12, 6))
observations_by_year = df['year'].value_counts().sort_index()

plt.subplot(1, 2, 1)
observations_by_year.plot(kind='bar', color='skyblue')
plt.title('Western Leopard Toad Observations by Year')
plt.xlabel('Year')
plt.ylabel('Number of Observations')
plt.xticks(rotation=45)


plt.subplot(1, 2, 2)
monthly_observations = df['month'].value_counts().sort_index()
month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
               'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
monthly_observations.index = [month_names[i-1] for i in monthly_observations.index]

monthly_observations.plot(kind='bar', color='lightgreen')
plt.title('Observations by Month (Seasonal Pattern)')
plt.xlabel('Month')
plt.ylabel('Number of Observations')
plt.tight_layout()
plt.show()