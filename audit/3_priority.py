import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# assuming 'data.csv' is your file
df = pd.read_csv('data.csv')

# Count the instances of each priority
priority_counts = df['Priority'].value_counts()

# Making a beautiful pie chart
plt.figure(figsize=(10,7))
color_palette = sns.color_palette("Set2")[:len(priority_counts)]
plt.pie(priority_counts, labels=priority_counts.index, colors=color_palette, autopct=lambda p: f'{p:.1f}%\n{int(round(p*sum(priority_counts)/100))}', startangle=140)
plt.title("Priority Distribution")
plt.tight_layout()

plt.savefig('aos/3_priority.png', dpi=300, bbox_inches='tight')