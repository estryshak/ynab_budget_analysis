import pandas as pd
import requests
import json

# get ynab_token from local file
ynab_token_df = pd.read_csv("ynab_token.txt", header=None)
ynab_token = ynab_token_df.iloc[0][0]

# get last knowledge of server variable from local file
last_knowledge_df = pd.read_csv("budget_last_knowledge_of_server.csv")
last_knowledge = last_knowledge_df.iloc[-1, 0]

my_headers = {"Authorization" : 'Bearer {}'.format(ynab_token)}
base_url = "https://api.youneedabudget.com/v1"


# get budget from api
budget_id = "9edc28cf-7cf4-40ea-84d4-2865cd23a66a"
budget_url = "/budgets/{}".format(budget_id)
last_knowledge_url ="?last_knowledge_of_server={}".format(last_knowledge)
budget_response = requests.get(base_url + budget_url, headers=my_headers)
budget_json = budget_response.json()


# write new last_knowledge_of_server value to file
with open("budget_last_knowledge_of_server.csv", "a") as fd:
    fd.write("\n" + str(budget_json["data"]["server_knowledge"]))

