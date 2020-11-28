import json
import os
import twitter
import time
import requests
import sys
import urllib3
from datetime import datetime

creds_file = sys.argv[1]
with open(creds_file, "r") as file:
    creds = json.load(file)

api = twitter.Api(consumer_key=creds["CONSUMER_KEY"],
                  consumer_secret=creds["CONSUMER_SECRET"],
                  access_token_key=creds["ACCESS_TOKEN"],
                  access_token_secret=creds["ACCESS_SECRET"],
                  sleep_on_rate_limit=True)


politicians_list = list()
path = './politicians2019/'

# with open(path, mode='r') as f:
#     politicians_list.extend([x for x in f.read().splitlines()])

for file in os.listdir(path):
    with open(path + file, mode='r') as f:
        politicians_list.extend([x for x in f.read().splitlines()])

error_num = 0
count = 0

x = datetime.now()
file_title = str(x.year) + x.strftime('%b') + '.edges'

with open(file_title, mode='a') as f:
    for politician in politicians_list:
        while True:
            try:
                followers = api.GetFollowerIDs(screen_name=politician)
            except (ConnectionResetError, requests.exceptions.ConnectionError, urllib3.exceptions.ProtocolError):
                # except (requests.exceptions.ConnectionError):
                print(f'error occured at {politician}')
                error_num += 1
                time.sleep(15 * 60)
            else:
                break
        for follower in followers:
            f.write(f"{follower},{politician}\n")
        # print(politician, ' Done')
        count += 1
        print(count)

print('All done')
print('errors: ', error_num)
