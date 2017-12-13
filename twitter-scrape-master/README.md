## Installation

* `pip install -r requirements.txt`

## Setup

* Create a file called `private.py`.
* Set the following keys in `private.py`.
    * `TWITTER_KEY`
    * `TWITTER_SECRET`
    * `TWITTER_APP_KEY`
    * `TWITTER_APP_SECRET`
* Set the following key in `private.py`.
    * `CONNECTION_STRING` -- use `sqlite:///tweets.db` as a default.

## Usage

* `python scrape.py` to scrape.  Use `Ctrl + C` to stop.
* `python dump.py` to generate `tweets.csv`, which contains all the tweet data that was scraped.(Contains questions from 3 to 7)
* If you want to edit behavior, change settings in `settings.py`.