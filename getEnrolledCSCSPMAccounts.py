import requests
import json

def getBearer():

    try:
        url = "https://api.us-2.crowdstrike.com/oauth2/token"
        
        # enter your clientId and clientSecret here
        payload='client_id=[]&client_secret=[]'
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/x-www-form-urlencoded'
            }
        response = requests.request("POST", url, headers=headers, data=payload)
        json = response.json()
        token = json['access_token']
        return token
    except:
        print("Could not connect to endpoint")

def getAccounts():
    try:
        url = "https://api.us-2.crowdstrike.com/cloud-connect-cspm-aws/entities/account/v1"
        payload={}
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
            'authorization': 'Bearer {}'.format(token)
            }
        response = requests.request("GET", url, headers=headers)
        accounts = response.json()
        return accounts
    except:
        print("Error")

if __name__ == "__main__":
# gets the token for the OAuth
    token = getBearer()
# gets the json
    accounts_json = getAccounts()

# you can display the keys in the json using the .keys() when you create the dict
# this create the dictionary for the enrolled accounts
    accounts_info_dict = accounts_json['resources']

    print("\nCurrent Accounts Enrolled in CrowdStrike CSPM")
    print('-' * 50)
    for i in accounts_info_dict:
        print(i['account_id'])

    print('-' * 50)
