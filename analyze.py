from functools import *
import json

with open("tweets.json", "r") as tweet_db:
    tweets = json.load(tweet_db)

def flatten(xs):
    return reduce(lambda x,y: x + y, xs)

def difference(xs, ys):
    return list(set(xs).symmetric_difference(set(ys)))

def to_text(tweets):
    return list(map(lambda x: x['content'], tweets))

def to_lowercase(tweets):
    return list(map(lambda x,y: {**x,**y}, tweets.copy(), list(map(lambda x: {**x, **{'content': x['content'].lower()}}, tweets)) ))

def nonempty(tweets):
    return list(map(lambda x, y: {**x, **y}, tweets.copy(), (list(filter(lambda x: len(x['content'])>0, tweets)))))

def total_word_count(tweets):
    return (reduce(lambda x,y: x + y, (list(map(lambda x: len(x['content'].split()), tweets)))))

def hashtags(tweet):
    return list(filter(lambda x: x.startswith('#'), tweet['content'].split()))

def mentions(tweet):
    return list(filter(lambda x: x.startswith('@'), tweet['content'].split()))

def all_hashtags(tweets):
    return flatten(list(map(lambda x: hashtags(x), tweets)))

def all_mentions(tweets):
    return flatten(list(map(lambda x: mentions(x), tweets)))

def all_caps_tweets(tweets):
    return (list(filter(lambda x: x['content'].isupper(), tweets)))

def count_individual_words(tweets):
    return (reduce(lambda x,y: dict(x, **y), (list(map(lambda x: {**{x: (flatten(list(map(lambda x: x.split(), to_text(tweets))))).count(x)}}, (flatten(list(map(lambda x: x.split(), to_text(tweets))))))))))

def count_individual_hashtags(tweets):
    if(len(all_hashtags(tweets)) == 0): return {}
    return (reduce(lambda x, y: dict(x, **y), (list(map(lambda x: {**{x: all_hashtags(tweets).count(x)}}, all_hashtags(tweets))))))

def count_individual_mentions(tweets):
    if(len(all_mentions(tweets)) == 0): return {}
    return (reduce(lambda x, y: dict(x, **y), (list(map(lambda x: {**{x: all_mentions(tweets).count(x)}}, all_mentions(tweets))))))

def n_most_common(n, word_count):
    return (sorted(dict(sorted(word_count.items(), key = lambda x: x[0])).items(), key=lambda x: x[1], reverse=True)[:n])

def iphone_tweets(tweets):
    return list(filter(lambda x: x['source'] == 'Twitter for iPhone', tweets))

def android_tweets(tweets):
    return list(filter(lambda x: x['source'] == 'Twitter for Android', tweets))

def average_favorites(tweets):
    return int((reduce(lambda x,y: x + y, (list(map(lambda x: (x['favorites']), tweets)))))/len((list(map(lambda x: (x['favorites']), tweets)))))

def average_retweets(tweets):
    return int((reduce(lambda x, y: x + y, (list(map(lambda x: (x['retweets']), tweets))))) / len((list(map(lambda x: (x['retweets']), tweets)))))

def sort_by_favorites(tweets):
    return (sorted(tweets, key = lambda x: x['favorites']))

def sort_by_retweets(tweets):
    return (sorted(tweets, key=lambda x: x['retweets']))

def upper_quartile(tweets):
    return tweets[round(0.75*len(tweets))]

def lower_quartile(tweets):
    return tweets[round(0.25 * len(tweets))]

def top_quarter_by(tweets, factor):
    if(factor == 'retweets'):
        return (list(filter(lambda x: x['retweets'] >= (upper_quartile(tweets)['retweets']), tweets)))
    if (factor == 'favorites'):
        return (list(filter(lambda x: x['favorites'] >= (upper_quartile(tweets)['favorites']), tweets)))

def bottom_quarter_by(tweets, factor):
    if (factor == 'retweets'):
        return (list(filter(lambda x: x['retweets'] >= (lower_quartile(tweets)['retweets']), tweets)))
    if (factor == 'favorites'):
        return (list(filter(lambda x: x['favorites'] >= (lower_quartile(tweets)['favorites']), tweets)))

