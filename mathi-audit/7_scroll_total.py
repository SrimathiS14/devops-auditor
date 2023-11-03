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

# Count the instances of each entry type
entry_type_counts = df['entry_type'].value_counts()

# Plot the bar chart
plt.figure(figsize=(10,6))
sns.set(style="whitegrid")
barplot = sns.barplot(x=entry_type_counts.index, y=entry_type_counts.values, palette="pastel")

# Add count text above each bar
for i, v in enumerate(entry_type_counts.values):
    barplot.text(i, v + 0.5, str(v), ha='center')

# Set title and labels
plt.title('Count of Each Entry Type')
plt.xlabel('Entry Type')
plt.ylabel('Count')

plt.tight_layout()
plt.savefig('aos/7_scroll_total.png', dpi=300, bbox_inches='tight')