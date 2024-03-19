import json
import requests
import pandas as pd
import re
from datetime import datetime
import sys


hashtag = sys.argv[1]
URL = f'https://mastodon.social/api/v1/timelines/tag/{hashtag}'

params = {
    'limit': 40
}
since_str=  sys.argv[2] ###"2023-11-15"
since = datetime.strptime(since_str, "%Y-%m-%d")
till_str=  sys.argv[3] ###"2023-11-17"
till = datetime.strptime(till_str, "%Y-%m-%d")
results = []
is_end = False

while True:
    r = requests.get(URL, params=params)
    toots = json.loads(r.text)
    
    for t in toots:
            t_txt = json.dumps(t)
            date = re.findall(r"created\_at\": \"([0-9-]+)[^\"]+\"\, \"in\_reply", t_txt)
            #print(date)
            if date:  # Check if the date list is not empty
                date_str = date[0]
                #print(date_str)
                date = datetime.strptime(date_str, "%Y-%m-%d")
                print(date, since_str)
                if date >= since and date < till:
                    results.append(t)
                elif date_str < since_str:
                    is_end = True
                    break
            else:
                print("No date found in tweet:", t_txt)

    if is_end:
            break

    if toots and date:  # Check if the 'toots' list is not empty
        max_id = toots[-1]['id']
        params['max_id'] = max_id
    else:
        print("No tweets found")
        break
        

#df = pd.DataFrame(results)

df = pd.DataFrame(results, columns=["created_at", "content", "language"])
df.to_csv('temp/x.tsv', sep="\t", index=False)
