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
params = {}
req = twitter.get(url_base + "statuses/home_timeline.json", params = params)


if req.status_code == 200:
    timeline = json.loads(req.text)
    # 各ツイートの本文を表示
    for tweet in timeline:
        print(tweet["text"].encode('utf-8'))

else:
    print ("Error: %d" % req.status_code)
