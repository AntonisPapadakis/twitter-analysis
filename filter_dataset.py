import twitter
import json
import os


def main():
    api = auth()

    path = './politicians2020/'
    ids = get_ids(path, api)

    dataset = 'edges/2020Dec.edges'
    filter_dataset(dataset, ids.values())


def auth():
    with open("twitter_credentials.json", "r") as file:
        creds = json.load(file)
    api = twitter.Api(consumer_key=creds["CONSUMER_KEY"],
                      consumer_secret=creds["CONSUMER_SECRET"],
                      access_token_key=creds["ACCESS_TOKEN"],
                      access_token_secret=creds["ACCESS_SECRET"],
                      sleep_on_rate_limit=True)
    return api


def get_ids(path, api):
    usernames = list()
    ids = dict()

    for file in os.listdir(path):
        with open(path + file, mode='r') as f:
            usernames.extend([x for x in f.read().splitlines()])

    for politician in usernames:
        ids[politician] = api.GetUser(screen_name=politician).id_str
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
