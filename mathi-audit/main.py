import pandas as pd
import aos_audit
import door_audit
import en_audit
# import pcr_audit

# Read the CSV file
aos_df = pd.read_csv('data.csv')
door_df = pd.read_csv('door.csv')
en_df = pd.read_csv('en.csv')
pcr_df = pd.read_csv('pcr.csv')

if __name__ == '__main__':
    aos_audit.category(aos_df)
    aos_audit.assignee(aos_df)
    aos_audit.priority(aos_df)
    aos_audit.response()
    aos_audit.resolution(aos_df)
    aos_audit.date_count()
    aos_audit.scroll_total(aos_df)
    aos_audit.each_scroll(aos_df)
    aos_audit.requester(aos_df)
    aos_audit.each_category(aos_df)
    aos_audit.card_status(aos_df)
    door_audit.status(door_df)
    door_audit.requester(door_df)
    door_audit.scroll(door_df)
    en_audit.environment(en_df)
    en_audit.request_type(en_df)
    pcr_audit.status(pcr_df)
    pcr_audit.requester(pcr_df)
