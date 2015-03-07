# coding: utf-8

import tweepy

CK = 'CmSPnXcyDwQPB0x2QrHVA'                             # Consumer Key
CS = 'tfEIhvelfw2b15j559jpJ9VHkPu9EK8ch483PfKoa1k'         # Consumer Secret
AT = '185165069-CKBQrdTWN2wj77H04xzD6upl9wOSJMcoy28b0x6a' # Access Token
AS = 'eyVPQ7ahtREEU34JVOfqxI8zi1P7mLJJs4K2Nd36v8H8n'         # Accesss Token Secert

# ツイート投稿用のURL
URL_BASE = "https://api.twitter.com/1.1/"
URL_SEARCH = URL_BASE + "search/tweets.json?"
#URL_TL = URL_BASE + "user.json"
URL_TL = "https://userstream.twitter.com/1.1/user.json"


# Twitterオブジェクトの生成
auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, AS)

class Listener(tweepy.StreamListener):
    def on_status(self, status):
        status.created_at += timedelta(hours=9)#世界標準時から日本時間に
        
        print('------------------------------')
        print(status.text)
        print("@" + str(status.author.screen_name))
        return True
    
    def on_error(self, status_code):
        print('Got an error with status code: ' + str(status_code))
        return True
    
    def on_timeout(self):
        print('Timeout...')
        return True



# Twitterオブジェクトの生成
twiobj = tweepy.OAuthHandler(CK, CS)
twiobj.set_access_token(AT, AS)

listener = Listener()
stream = tweepy.Stream(twiobj, listener)
stream.userstream()
#stream.filter(track=["テスト"])
#stream.sample()