# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 00:30:03 2021

@author: Deepti
"""



import requests

import json


# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "bxlj9AG3rsG1Qz7n5BmbUOr_rdpRindmfNjGWlhvZ5pu"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]
print("mltoken",mltoken)

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
#payload_scoring = {"input_data": [{"field": [array_of_input_fields],"values":[array_of_values_to_be_scored, another_array_of_values_to_be_scored]}]}
payload_scoring = {"input_data":[["Current Loan Amount","Term","Credit Score","Annual Income","Years in current job","Home Ownership","Years of Credit History","Number of Credit Problems","Bankruptcies","Tax Liens","Credit Problems","Credit Age"]],
                   "values": [[0.21538779, -0.62204006, -0.25995262, -0.37673145, 
                              -1.15886448,-0.97633895, -0.59844981, -0.34869095,
                              -0.33391075, -0.10969543,-0.39894497,  0.98973021]]}
response_scoring = requests.post('https://eu-gb.ml.cloud.ibm.com/ml/v4/deployments/53a3efba-c3eb-4288-9edc-59510fec724f/predictions?version=2021-08-07', json=payload_scoring, headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
print(response_scoring.json())
