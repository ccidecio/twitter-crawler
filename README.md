
# Twitter Crawler

This repository contains a tweet crawler for Twitter. One can search queries with or without hashtags, can modify the date (database reachability depends on the app limits and app API type), language and tweet quantity limits. 

## Getting Started

To be able to search and crawl tweets, one needs to create a Twitter account. Then apply for a developer account for access to developer APIs. After the authentication process Twitter creates API and access keys for specific apps. These keys are a **required** to access Twitter database. For privacy and security reasons, they are hidden in the code. 

Turkish version of these instructions is available as a [PDF](twitter_registration_guide(tr).pdf) in detailed fashion.

### Prerequisites

This code uses a wrapper for convenience:

```
tweepy
```

### Installing

Installation is fairly straightforward:

Install [tweepy](https://www.tweepy.org/) using pip: 

```
pip install tweepy
```

or if one needs to work on Anaconda:

```
conda install -c anaconda tweepy
```

## Notes:

In the case of excessive requests or lack of tweets with the specific query, may result in time-outs. In these situations, one may try to wait for an arbitrary period, then try again or send the requests with delays between them. 

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
