import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the data
df = pd.read_csv('data.csv')

# Function to categorize entries
def categorize_entry(entry):
    if pd.isnull(entry):
        return 'Without Scroll'
    elif str(entry).startswith('[http'):
        return 'Scroll'
    else:
        return 'Not Required'

# Create a new column 'entry_type' using the 'categorize_entry' function
df['entry_type'] = df['Enter Scroll here'].apply(categorize_entry)

# Group the data by Assignee and Entry type and count the occurrences
entry_type_counts = df.groupby(['Assignee.Name', 'entry_type']).size().unstack(fill_value=0)

# Calculate the total counts for each assignee
entry_type_counts['Total'] = entry_type_counts.sum(axis=1)

# Sort assignees based on total counts (descending order)
entry_type_counts = entry_type_counts.sort_values('Total', ascending=False)

# Plot the bar chart
entry_type_counts.drop(columns='Total').plot(kind='bar', stacked=True, figsize=(12, 8), colormap='Set3')

# Set title and labels
plt.title('Entries per Assignee by Entry Type')
plt.xlabel('Assignee')
plt.ylabel('Count')

# Rotate x-axis labels
plt.xticks(rotation=45, ha='right')

plt.tight_layout()
plt.savefig('aos/8_each_scroll.png', dpi=300, bbox_inches='tight')