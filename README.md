# mastodon-scrape

Scraping toots from Mastodon without any authentification


## Requeriments:
* Bash and Python3
* Python modules: panda, requests, json (use `pip install`) 

## How to use:

* Module `timeline`: this module uses hashtags to retrieve toots over time, starting with the present and looking backwards. You need to specify a hashtag/keyword (for instance `-k putin`) and a specific period of time: for instance: `-s 2023-11-18 -t 2023-11-19`. This is a possible query:

```./mastodon -m timeline -k putin -s 2023-11-18 -t 2023-11-19```

*  With the module `timeline', you can use language selection (pt, en, gl, es, ...):

```./mastodon -m timeline -k putin -s 2023-11-18 -t 2023-11-19 -l en```

* Module `search`: retrieve toots using a keyword. It only allows you to extract 40 toots for each search:

```./mastodon -m search -k trump```

