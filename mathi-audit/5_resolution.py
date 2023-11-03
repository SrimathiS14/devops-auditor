import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# read the data
data = pd.read_csv('data.csv')

# Convert the Resolution time from seconds to hours
data['Resolution time'] = data['Resolution time'] / 3600 

# Set the figure size and style
plt.figure(figsize=[12, 8])
sns.set(style="whitegrid")

# Boxplot visualization
sns.boxplot(data['Resolution time'], color='skyblue', width=0.4)

# Adding stripplot with adjusted jitter
sns.stripplot(data['Resolution time'], color='black', size=4, jitter=0.2)

# Set y-axis range

# Set the title and labels
plt.title('Distribution of Resolution Time')
plt.xlabel('Resolution Time (in hours)')

plt.savefig('aos/5_resolution.png', dpi=300, bbox_inches='tight')