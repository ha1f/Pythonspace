#!/usr/bin/env python
# -*- coding: utf-8 -*-

from requests_oauthlib import OAuth1Session

CK = 'FpkNLROiYwdlvJv4XXFQPoHE2'                          # Consumer Key
CS = '7tMpc3aTmI7vBjIAtROwXC0aDbEUUCuHG5LvSryIvHYhEZk2pD' # Consumer Secret
AT = '185165069-AcjWMscVJrGPoyzMjl1NXZDCxxmc9TWPnKMhJIsN' # Access Token
AS = '22sQ1FoNf0AEZ6CuqLBGXbEjEbLeGoofagrX529VH70hh'      # Accesss Token Secert

# ツイート投稿用のURL
url = "https://api.twitter.com/1.1/statuses/update.json"

textlist = ["1","2","3"]

twitter = OAuth1Session(CK, CS, AT, AS)

for stringdata in textlist:
    params = {"status": stringdata}
    req = twitter.post(url, params = params)
    if req.status_code == 200:
        print ("OK")
    else:
        print ("Error: %d" % req.status_code)
