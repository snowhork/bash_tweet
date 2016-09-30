### bash_tweet

ターミナル上で、ツイッターAPIを簡単に叩けるようにして、
タイムラインが見えるようにするためのもの。

## alias for .bashrc

ターミナル上で、twでツイートしたい人は.bashrcか.bash_profileに以下を書き加える

function _post_tweet() {
    python post_tweet.py $1
    
}

alias tw='_post_tweet'

## NOTE

http://kivantium.hateblo.jp/entry/2015/01/03/000225

1.↑を参考にaccess tokenを登録する

2. pytter.pyを以下のように作り、PYTHONPATHを通しておく。

--- pytteer.py---
#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Tweepyライブラリをインポート
import tweepy

def create_api():
    # 各種キーをセット
    CONSUMER_KEY = hogehoge
    CONSUMER_SECRET = hogehoge
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    ACCESS_TOKEN = hogehoge
    ACCESS_SECRET = hogehoge
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    return tweepy.API(auth)


