import tweepy
import json
import os

with open("twitter_credentials.json", "r") as file:
    creds = json.load(file)

auth = tweepy.OAuthHandler(creds["CONSUMER_KEY"], creds["CONSUMER_SECRET"])
auth.set_access_token(creds["ACCESS_TOKEN"], creds["ACCESS_SECRET"])

api = tweepy.API(auth, wait_on_rate_limit=True)

usernames = list()
ids = list()
path = './politicians2019/'

for file in os.listdir(path):
    with open(path + file, mode='r') as f:
        usernames.extend([x for x in f.read().splitlines()])

for politician in usernames:
    ids.append(api.get_user(politician).id_str)

with open('new.edges', mode='r') as f:
    edges = f.read().splitlines()

with open('noi.edges', mode='w') as f:
    for edge in edges:
        if edge.split(',')[0] not in ids:
            f.write(edge + '\n')

with open('noi_to_noi.edges', mode='w') as f:
    for edge in edges:
        if edge.split(',')[0] in ids:
            f.write(edge + '\n')
