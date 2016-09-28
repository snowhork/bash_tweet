### bash_tweet

ターミナル上で、ツイッターAPIを簡単に叩けるようにして、
タイムラインが見えるようにするためのもの。

## alias for .bashrc

function _post_tweet() {
    python post_tweet.py $1
    
}

alias tw='_post_tweet'

## NOTE

pytterは自作ライブラリで、ただ単にtweepyを用いてAPIを叩けるようにしてるだけで隠蔽しているだけ。