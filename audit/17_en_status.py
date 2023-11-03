# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the csv file
df = pd.read_csv('en.csv')

# Count the frequency of each resource type
resource_counts = df['Status'].value_counts()

# Create a bar plot
plt.figure(figsize=(10,6))
barplot = sns.barplot(x=resource_counts.index, y=resource_counts.values, alpha=0.8)

# Add the total counts on top of each bar
for p in barplot.patches:
    barplot.annotate(format(p.get_height(), '.1f'), 
                     (p.get_x() + p.get_width() / 2., p.get_height()), 
                     ha = 'center', va = 'center', 
                     xytext = (0, 9), 
                     textcoords = 'offset points')

plt.title('Status Distribution of Resource Types')
plt.ylabel('Number of Occurrences', fontsize=12)
plt.xlabel('Status Type', fontsize=12)
plt.xticks(rotation=90)
plt.tight_layout()  # To ensure that the labels are not cut-off
plt.savefig('en/3_status.png', dpi=300, bbox_inches='tight')