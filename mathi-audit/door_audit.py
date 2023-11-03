import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the CSV file
# df = pd.read_csv('door.csv')

def status(df):
    # Set the style
    sns.set_style("whitegrid")
    sns.set_palette("Set2")

    # Count the occurrences of each mission category
    mission_category_counts = df['Status'].value_counts()

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
    plt.xlabel('Status')
    plt.ylabel('Count')
    plt.title('Total Number and Percentage of Status')

    # Rotate x-axis labels
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    # Show the chart
    plt.savefig('door-audit-images/1_door_status.png', dpi=300, bbox_inches='tight')

def requester(df):

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
    plt.savefig('door-audit-images/2_door_requester.png', dpi=300, bbox_inches='tight')

def scroll(df):

    # Function to categorize entries
    def categorize_entry(entry):
        if pd.isnull(entry):
            return 'Scroll'
        elif str(entry).startswith('[http'):
            return 'Scroll'
        else:
            return 'Without Scroll'

    # Create a new column 'entry_type' using the 'categorize_entry' function
    df['entry_type'] = df['Knowledge Base'].apply(categorize_entry)

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
    plt.savefig('door-audit-images/3_door_scroll.png', dpi=300, bbox_inches='tight')

# status(df)
# requester(df)
# scroll(df)