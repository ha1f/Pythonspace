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
        """ Prints tweet and hashtags """
        print('------------------------------')
        print(status.text)
            #for hashtag in status.entities['hashtags']:
            #print(hashtag['text']),
            #print("")
        return True
    
    def on_error(self, status_code):
        print('Got an error with status code: ' + str(status_code))
        return True
    
    def on_timeout(self):
        print('Timeout...')
        return True

listener = Listener()
stream = tweepy.Stream(auth, listener)
stream.filter(track=['#自分の絵柄の原点あげてけ'])