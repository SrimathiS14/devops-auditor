import pandas as pd
import matplotlib.pyplot as plt

# Read the data
df = pd.read_csv('data.csv')

# Group the data by 'Assignee.Name' and 'Mission Category' and count the occurrences
category_counts = df.groupby(['Assignee.Name', 'Mission Category']).size().unstack(fill_value=0)

# Calculate the total counts for each assignee
category_counts['Total'] = category_counts.sum(axis=1)

# Sort assignees based on total counts (descending order)
category_counts = category_counts.sort_values('Total', ascending=False)

# Drop the 'Total' column for visualization
category_counts = category_counts.drop(columns='Total')

# Plot the bar chart with matplotlib
category_counts.plot(kind='bar', stacked=True, figsize=(10, 7))

# Set title and labels
plt.title('Mission Category Counts for Each Assignee')
plt.xlabel('Assignee Name')
plt.ylabel('Count')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Layout Configuration
plt.tight_layout()
plt.savefig('aos/10_each_category.png', dpi=300, bbox_inches='tight')