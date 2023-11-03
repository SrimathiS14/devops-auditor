import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set the style
sns.set_style("whitegrid")
sns.set_palette("Set2")

# Read the CSV file
df = pd.read_csv('data.csv')

# Count the occurrences of each mission category
mission_category_counts = df['Mission Category'].value_counts()

# Calculate the percentage of each category
total_count = mission_category_counts.sum()
percentage = mission_category_counts / total_count * 100

# Plot the chart
plt.figure(figsize=(10, 6))
barplot = sns.barplot(x=mission_category_counts.index, y=mission_category_counts.values)

# Add percentage text on top of each bar
for p, label in zip(barplot.patches, percentage):
    height = p.get_height()
    barplot.text(p.get_x() + p.get_width() / 2, height + 5, f'{label:.1f}%', ha='center')

# Set labels and title
plt.xlabel('Mission Category')
plt.ylabel('Count')
plt.title('Total Number and Percentage of Mission Categories')

# Rotate x-axis labels
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Save the chart
plt.savefig('aos/1_category.png', dpi=300, bbox_inches='tight')