import json
import time


i=0
l=[0]
while True:
    with open('data.txt', 'w') as outfile:
        i=i+1
        l=l+[i]
        json.dump(l, outfile)
    time.sleep(1)