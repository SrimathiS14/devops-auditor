import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the data
df = pd.read_csv('data.csv')

# Count the instances of each assignee
assignee_counts = df['Requester.Name'].value_counts()

# Plot the bar chart
plt.figure(figsize=(12, 8))
sns.set(style="whitegrid")
barplot = sns.barplot(x=assignee_counts.index, y=assignee_counts.values, palette="Set2")

# Add count text above each bar
for i, v in enumerate(assignee_counts.values):
    barplot.text(i, v + 0.5, str(v), ha='center')

# Rotate x-axis labels
plt.xticks(rotation=45, ha='right')

# Set labels and title
plt.title('Total Count of Each Requester')
plt.xlabel('Requester')
plt.ylabel('Count')

plt.tight_layout()

# Show the chart
plt.savefig('aos/9_requester.png', dpi=300, bbox_inches='tight')