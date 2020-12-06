import json
import os
import sys
import time
from datetime import datetime

import requests
import twitter
import urllib3


def main():
    if len(sys.argv) > 1 and sys.argv[1] == '--help':
        print("""
            Exactly 2 arguments needed.
            1st: JSON file with Twitter API credentials.
                    Keys should be: "consumer_key", "consumer_secret", "access_token_key", "access_token_secret"
            2nd: txt file with the usernames of all the accounts whose followers you want to download.
                    Each username should be in a seperate line   
                """)
        return
    if len(sys.argv) != 3:
        print('Exactly 2 arguments needed. Use "tool.py --help" for more info')
        return

    credentials = sys.argv[1]
    accounts_file_path = sys.argv[2]

    api = auth(credentials)
    accounts_list = read(accounts_file_path)

    date = datetime.now()
    file_name = str(date.year) + date.strftime('%b') + '.edges'
    count = 0

    for account in accounts_list:
        followers = download(account, api)
        with open(file_name, mode='a') as f:
            for follower in followers:
                f.write(f"{follower},{account}\n")
        count += 1
        print(count)

    print('All done')
    # print("--- %s seconds ---" % (time.time() - start_time))


def auth(credentials):
    with open(credentials, "r") as file:
        creds = json.load(file)
    api = twitter.Api(consumer_key=creds["consumer_key"],
                      consumer_secret=creds["consumer_secret"],
                      access_token_key=creds["access_token_key"],
                      access_token_secret=creds["access_token_secret"],
                      sleep_on_rate_limit=True)
    try:
        api.VerifyCredentials()
        return api
    except twitter.error.TwitterError as e:
        print('Wrong credentials:', e)
        exit(-1)


def read(file):
    accounts_list = list()
    with open(file, mode='r') as f:
        accounts_list.extend([x for x in f.read().splitlines()])
    return accounts_list


def download(account, api):
    while True:
        try:
            print(account)
            followers = api.GetFollowerIDs(screen_name=account)
        # except (ConnectionResetError, requests.exceptions.ConnectionError, urllib3.exceptions.ProtocolError):
        except (requests.exceptions.ConnectionError):
            print(f'error occured at {account}')
            time.sleep(600)
        else:
            break
    return followers


if __name__ == '__main__':
    main()
