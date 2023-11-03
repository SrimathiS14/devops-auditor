import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# assuming 'data.csv' is your file
df = pd.read_csv('data.csv', parse_dates=['Created at'])

# Extract date from 'created at' and create a new column 'Date'
df['Date'] = df['Created at'].dt.date

# group by 'Date' and count the instances (cards) for each date
df['Cards'] = df.groupby('Date')['Date'].transform('count')

# Set the theme
sns.set_theme()

# Create a bar plot
plt.figure(figsize=(12, 8))
chart = sns.barplot(x='Date', y='Cards', data=df)
chart.set_xticklabels(chart.get_xticklabels(), rotation=45)
plt.title('Total number of cards handled by date')
plt.xlabel('Date')
plt.ylabel('Number of cards')

# Display the chart
plt.savefig('aos/6_date_count.png', dpi=300, bbox_inches='tight')