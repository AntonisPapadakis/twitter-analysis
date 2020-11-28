import os

path = './politicians2019/'

for file in os.listdir(path):
    hubs = []
    with open(path+file, mode='r') as f:
        hubs.extend([x for x in f.read().splitlines()])
    with open('truth.txt', mode='a') as new_file:
        for hub in hubs:
            new_file.write(hub + ' ')
        new_file.write('\n')

print('Done')
