import json
import time

while True:
    with open('data.txt', 'r') as infile:
        l=json.load( infile)
        print(l)
    time.sleep(0.5)