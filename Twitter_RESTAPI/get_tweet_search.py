# -*- coding: utf-8 -*-

from requests_oauthlib import OAuth1Session
import json

CK = ''# Consumer Key
CS = ''# Consumer Secret
AT = ''# Access Token
AS = ''# Accesss Token Secert

# ツイート投稿用のURL
url_base = "https://api.twitter.com/1.1/"


# Twitterオブジェクトの生成
twitter = OAuth1Session(CK, CS, AT, AS)


#TLの取得
params = {
    "q": u'モス',
    "lang": 'ja',
    "result_type": 'recent',
    "count": '200'
    }
req = twitter.get(url_base + "search/tweets.json?", params = params)


if req.status_code == 200:
    tweets = json.loads(req.text)
    for tweet in tweets['statuses']:
        print tweet['text'].encode('utf-8')
else:
    print ("Error: %d" % req.status_code)

"""
'search_metadata'
    count
    completed_in
    max_id_str
    since_id_str
    next_results
    refresh_url
    since_id
    query
    max_id
'statuses'
    'contributors'
    'truncated'
    'text'
    'in_reply_to_status_id'
    'id', u'favorite_count'
    'source', u'retweeted'
    'coordinates'
    'entities'
    'in_reply_to_screen_name'
    'in_reply_to_user_id'
    'retweet_count'
    'id_str'
    'favorited'
    'user'
    'geo'
    'in_reply_to_user_id_str'
    'possibly_sensitive'
    'lang'
    'created_at'
    'in_reply_to_status_id_str'
    'place'
    'metadata'
    """
