# -*- coding: utf-8 -*-

from requests_oauthlib import OAuth1Session
import json

CK = 'FpkNLROiYwdlvJv4XXFQPoHE2'                             # Consumer Key
CS = '7tMpc3aTmI7vBjIAtROwXC0aDbEUUCuHG5LvSryIvHYhEZk2pD'         # Consumer Secret
AT = '185165069-AcjWMscVJrGPoyzMjl1NXZDCxxmc9TWPnKMhJIsN' # Access Token
AS = '22sQ1FoNf0AEZ6CuqLBGXbEjEbLeGoofagrX529VH70hh'         # Accesss Token Secert

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
