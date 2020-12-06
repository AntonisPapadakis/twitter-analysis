import tweepy
import json
import os


def main():
    api = tweepy_auth()

    path = './politicians2020/'
    ids = get_ids(path, api)

    dataset = 'edges/2020Dec.edges'
    filter_dataset(dataset, ids.values())


def tweepy_auth():
    with open("twitter_credentials.json", "r") as file:
        creds = json.load(file)
    auth = tweepy.OAuthHandler(creds["CONSUMER_KEY"], creds["CONSUMER_SECRET"])
    auth.set_access_token(creds["ACCESS_TOKEN"], creds["ACCESS_SECRET"])
    api = tweepy.API(auth, wait_on_rate_limit=True)
    return api


def get_ids(path, api):
    usernames = list()
    ids = dict()

    for file in os.listdir(path):
        with open(path + file, mode='r') as f:
            usernames.extend([x for x in f.read().splitlines()])

    for politician in usernames:
        # ids.append(api.get_user(politician).id_str)
        ids[politician] = api.get_user(politician).id_str

    return ids


def filter_dataset(dataset, ids):
    with open(dataset, mode='r') as f:
        edges = f.read().splitlines()

    with open('noi.edges', mode='w') as f:
        for edge in edges:
            if edge.split(',')[0] not in ids:
                f.write(edge + '\n')

    with open('noi_to_noi.edges', mode='w') as f:
        for edge in edges:
            if edge.split(',')[0] in ids:
                f.write(edge + '\n')


if __name__ == '__main__':
    main()
    print('done')
