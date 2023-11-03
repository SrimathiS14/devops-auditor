import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load .csv file to DataFrame
df = pd.read_csv('en.csv')

# Count occurrences of each 'Environment'
env_counts = df['Environment'].value_counts().reset_index()
env_counts.columns = ['Environment', 'Counts']

# Visualization
plt.figure(figsize=(8, 4))
sns.barplot(data=env_counts, x='Environment', y='Counts')
plt.title('Environment vs Number of Requests')
plt.savefig('en/1_environment.png', dpi=300, bbox_inches='tight')