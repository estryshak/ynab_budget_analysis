import pandas as pd
import json

# JSON FORMAT
# data {
#     budget {
#         accounts
#         payees
#         category_groups
#         categories
#         months {
#           categories
#           }
#         transactions
#         subtransactions
#         scheduled_transactions
#     }
# }

# get most recent file time
last_data_pull_df = pd.read_csv('last_data_pull.csv')
last_data_pull = last_data_pull_df.iloc[-1, 0]

# read in json file
f = open('budget-' + last_data_pull + '.json')
data = json.load(f)

# get months data dict
dict_months = data['data']['budget']['months']

# init list
months_list = []

for m in dict_months:
    mon = m['month']
    for cat in m['categories']:
        category_name = cat['name']
        budgeted = cat['budgeted']
        activity = cat['activity']
        balance = cat['balance']
        
        # create temp list to concat
        new_row = [mon, category_name, budgeted, activity, balance]
        # concat row to dataframe
        months_list.append(new_row)

# convert to dataframe
df_months = pd.DataFrame(months_list,
                         columns=['month','category_name', 'budgeted', 'activity', 'balance'])

# output to csv
df_months.to_csv('month-category.csv', index=False)
