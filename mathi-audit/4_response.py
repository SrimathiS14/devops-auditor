import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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
plt.savefig('/Users/srimathis/Downloads/audit-automation/dummy/page-response.png', dpi=300, bbox_inches='tight')