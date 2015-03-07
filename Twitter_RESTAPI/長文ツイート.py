#!/usr/bin/env python
# -*- coding: utf-8 -*-

from requests_oauthlib import OAuth1Session

CK = 'FpkNLROiYwdlvJv4XXFQPoHE2'                          # Consumer Key
CS = '7tMpc3aTmI7vBjIAtROwXC0aDbEUUCuHG5LvSryIvHYhEZk2pD' # Consumer Secret
AT = '185165069-AcjWMscVJrGPoyzMjl1NXZDCxxmc9TWPnKMhJIsN' # Access Token
AS = '22sQ1FoNf0AEZ6CuqLBGXbEjEbLeGoofagrX529VH70hh'      # Accesss Token Secert

# ツイート投稿用のURL
url = "https://api.twitter.com/1.1/statuses/update.json"

longtext = u"眠くない"

to = ["","","","","","","","","",""]
tonum = 0

textandtag = longtext
for i in range(0,10):
    if textandtag[0] == u"@":
        to[i],textandtag = textandtag.split(" ",1)
    else:
        break

"""
tostr = u""
for stringdata in to:
    if stringdata != u"":
        tostr = tostr + stringdata + u" "

tags = textandtag.split(u" #")
text = tags.pop(0)#左を取り出す
"""
text, tagstr = textandtag.split(u" #",1)

tagstr = u""
for stringdata in tags:
    if stringdata != u"":
        tagstr = tagstr + u" #" + stringdata

textarea = 140 - (len(tagstr) + len(tostr))

textlist = []

if len(text) > textarea:#書ききれない
    textarea=textarea-6# (k/n)の部分
    num = int(len(text)/textarea) + 1
    for i in range(0,num):
        tweet = tostr.encode('utf-8') + text[(textarea*i):(textarea*(i+1))].encode('utf-8') + " (" + str(i+1) + "/" + str(num) + ")" + tagstr.encode('utf-8')
        textlist.append(tweet)
        print tweet
else:
    textlist = [longtext]
    print longtext.encode('utf-8')



twitter = OAuth1Session(CK, CS, AT, AS)

for stringdata in textlist:
    params = {"status": stringdata}
    req = twitter.post(url, params = params)
    if req.status_code == 200:
        print ("OK")
    else:
        print ("Error: %d" % req.status_code)



