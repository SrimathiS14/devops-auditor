import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load .csv file to DataFrame
# df = pd.read_csv('en.csv')

def environment(df):
    # Count occurrences of each 'Environment'
    env_counts = df['Environment'].value_counts().reset_index()
    env_counts.columns = ['Environment', 'Counts']

    # Visualization
    plt.figure(figsize=(8, 4))
    sns.barplot(data=env_counts, x='Environment', y='Counts')
    plt.title('Environment vs Number of Requests')
    plt.savefig('en-audit-images/1_environment.png', dpi=300, bbox_inches='tight')

def request_type(df):
    # Count the frequency of each resource type
    resource_counts = df['Resource Type'].value_counts()

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

    plt.title('Frequency Distribution of Resource Types')
    plt.ylabel('Number of Occurrences', fontsize=12)
    plt.xlabel('Resource Type', fontsize=12)
    plt.xticks(rotation=90)
    plt.tight_layout()  # To ensure that the labels are not cut-off
    plt.savefig('en-audit-images/2_request_type.png', dpi=300, bbox_inches='tight')

# environment(df)
# request_type(df)