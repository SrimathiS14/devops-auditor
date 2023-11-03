import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Read the CSV file
# df = pd.read_csv('data.csv')

def category(df):
    sns.set_style("whitegrid")
    sns.set_palette("Set2")

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
    plt.savefig('aos-audit-images/1_category.png', dpi=300, bbox_inches='tight')

def assignee(df):

    # Count the instances of each Assignee
    assignee_counts = df['Assignee.Name'].value_counts()

    plt.figure(figsize=[10,7])
    colors = sns.color_palette('pastel')[:len(assignee_counts)]
    plt.pie(assignee_counts, labels = assignee_counts.index, colors=colors, autopct=lambda p: f'{p:.1f}% ({int(p*sum(assignee_counts)/100)})', startangle=140)
    plt.title("Assignee Distribution")
    plt.tight_layout()

    plt.savefig('aos-audit-images/2_assigne.png', dpi=300, bbox_inches='tight')

def priority(df):

    # Count the instances of each priority
    priority_counts = df['Priority'].value_counts()

    # Making a beautiful pie chart
    plt.figure(figsize=(10,7))
    color_palette = sns.color_palette("Set2")[:len(priority_counts)]
    plt.pie(priority_counts, labels=priority_counts.index, colors=color_palette, autopct=lambda p: f'{p:.1f}%\n{int(round(p*sum(priority_counts)/100))}', startangle=140)
    plt.title("Priority Distribution")
    plt.tight_layout()

    plt.savefig('aos-audit-images/3_priority.png', dpi=300, bbox_inches='tight')

def response():
    # read csv file
    data = pd.read_csv('backlog.csv') 

    # convert seconds to minutes
    data['Time spent'] = data['Time spent'] / 60

    # creating td groups
    td_below_15 = data[data["Time spent"]<=15]
    td_above_15 = data[data["Time spent"]>15]

    # get total counts for both categories
    count_below_15 = len(td_below_15)
    count_above_15 = len(td_above_15)

    # # get percentage for each category
    # percentage_below_15 = count_below_15 / (count_below_15 + count_above_15) * 100
    # percentage_above_15 = count_above_15 / (count_below_15 + count_above_15) * 100

    # plot bar chart, color='blue' for 'Below or Equal to 15 minutes', color='orange' for 'Above 15 minutes'
    bars = plt.bar(['Below or Equal to 15 minutes', 'Above 15 minutes'], [count_below_15, count_above_15], color=['blue', 'orange'])

    # add count and percentage annotations on top of each bar
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 0.05,
                f'{int(yval)} ({round(yval/(count_below_15 + count_above_15)*100, 2)}%)',
                ha='center', va='bottom')

    plt.ylabel('Counts')
    plt.title('Time spent by groups')
    plt.savefig('aos-audit-images/4_response.png', dpi=300, bbox_inches='tight')

def resolution(df):
    # Convert the Resolution time from seconds to hours
    df['Resolution time'] = df['Resolution time'] / 3600 

    # Set the figure size and style
    plt.figure(figsize=[12, 8])
    sns.set(style="whitegrid")

    # Boxplot visualization
    sns.boxplot(df['Resolution time'], color='skyblue', width=0.4)

    # Adding stripplot with adjusted jitter
    sns.stripplot(df['Resolution time'], color='black', size=4, jitter=0.2)

    # Set y-axis range

    # Set the title and labels
    plt.title('Distribution of Resolution Time')
    plt.xlabel('Resolution Time (in hours)')

    plt.savefig('aos-audit-images/5_resolution.png', dpi=300, bbox_inches='tight')

def date_count():
    # assuming 'data.csv' is your file
    df = pd.read_csv('data.csv', parse_dates=['Created at'])

    # Extract date from 'created at' and create a new column 'Date'
    df['Date'] = df['Created at'].dt.date

    # group by 'Date' and count the instances (cards) for each date
    df['Cards'] = df.groupby('Date')['Date'].transform('count')

    # Set the theme
    sns.set_theme()

    # Create a bar plot
    plt.figure(figsize=(12, 8))
    chart = sns.barplot(x='Date', y='Cards', data=df)
    chart.set_xticklabels(chart.get_xticklabels(), rotation=45)
    plt.title('Total number of cards handled by date')
    plt.xlabel('Date')
    plt.ylabel('Number of cards')

    # Display the chart
    plt.savefig('aos-audit-images/6_date_count.png', dpi=300, bbox_inches='tight')

def scroll_total(df):

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
    barplot = sns.barplot(x=entry_type_counts.index, y=entry_type_counts.values, palette="pastel", legend=False)

    # Add count text above each bar
    for i, v in enumerate(entry_type_counts.values):
        barplot.text(i, v + 0.5, str(v), ha='center')

    # Set title and labels
    plt.title('Count of Each Entry Type')
    plt.xlabel('Entry Type')
    plt.ylabel('Count')

    plt.tight_layout()
    plt.savefig('aos-audit-images/7_scroll_total.png', dpi=300, bbox_inches='tight')

def each_scroll(df):
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
    plt.savefig('aos-audit-images/8_each_scroll.png', dpi=300, bbox_inches='tight')

def requester(df):

    # Count the instances of each assignee
    assignee_counts = df['Requester.Name'].value_counts()

    # Plot the bar chart
    plt.figure(figsize=(12, 8))
    sns.set(style="whitegrid")
    barplot = sns.barplot(x=assignee_counts.index, y=assignee_counts.values, palette="Set2", legend=False)

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
    plt.savefig('aos-audit-images/9_requester.png', dpi=300, bbox_inches='tight')

def each_category(df):
    # Group the data by 'Assignee.Name' and 'Mission Category' and count the occurrences
    category_counts = df.groupby(['Assignee.Name', 'Mission Category']).size().unstack(fill_value=0)

    # Calculate the total counts for each assignee
    category_counts['Total'] = category_counts.sum(axis=1)

    # Sort assignees based on total counts (descending order)
    category_counts = category_counts.sort_values('Total', ascending=False)

    # Drop the 'Total' column for visualization
    category_counts = category_counts.drop(columns='Total')

    # Plot the bar chart with matplotlib
    category_counts.plot(kind='bar', stacked=True, figsize=(10, 7))

    # Set title and labels
    plt.title('Mission Category Counts for Each Assignee')
    plt.xlabel('Assignee Name')
    plt.ylabel('Count')

    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45, ha='right')

    # Layout Configuration
    plt.tight_layout()
    plt.savefig('aos-audit-images/10_each_category.png', dpi=300, bbox_inches='tight')

def card_status(df):
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
    plt.savefig('aos-audit-images/11_card_status.png', dpi=300, bbox_inches='tight')

# category(df)
# assignee(df)
# priority(df)
# response()
# resolution(df)
# date_count()
# scroll_total(df)
# each_scroll(df)
# requester(df)
# each_category(df)
# card_status(df)