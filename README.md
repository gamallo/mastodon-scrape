# mastodon-scrape

Scrapping toots from Mastodon without any authentification


## Requeriments:
* Bash and Python3
* Python modules: panda, requests, json (use `pip install`) 

## How to use:

* Module `timeline`: retrieve toots using hashtags along a timeline You need to specify the hashtag or keyword and a specific period of time (since (-s)  to (-t).

```./mastodon -m timeline -k putin -s 2023-11-18 -t 2023-11-19```

*  With the module `timeline', you can use language selection (en, es, pt...):

```./mastodon -m timeline -k putin -s 2023-11-18 -t 2023-11-19 -l en```

* Module `search`: retrieve toots using a keyword. It only allows you to extract 40 toots for each search:

```./mastodon -m search -k putin```

