import requests
import json
import pandas as pd
import html2text
import sys


query = sys.argv[1]

url = f'https://mastodon.social/api/v2/search'

params = {
    'limit': 40,
    'q': query
}
results=[]
count=0
is_end = False

r = requests.get(url, params=params)
toots = json.loads(r.text)
print(toots)
for t in toots['accounts']:
  results.append(t)


df = pd.DataFrame(results, columns=["created_at", "note"])
df.to_csv('./temp/x.tsv', sep="\t", index=False)
