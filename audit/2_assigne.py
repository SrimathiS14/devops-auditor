import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the data
df = pd.read_csv('data.csv')

# Count the instances of each Assignee
assignee_counts = df['Assignee.Name'].value_counts()

plt.figure(figsize=[10,7])
colors = sns.color_palette('pastel')[:len(assignee_counts)]
plt.pie(assignee_counts, labels = assignee_counts.index, colors=colors, autopct=lambda p: f'{p:.1f}% ({int(p*sum(assignee_counts)/100)})', startangle=140)
plt.title("Assignee Distribution")
plt.tight_layout()

plt.savefig('aos/2_assigne.png', dpi=300, bbox_inches='tight')