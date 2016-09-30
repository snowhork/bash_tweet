#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import numpy as np
import time

import load_tweet.load_tweet as load_tweet
import display_tweet.display_tweet as display_tweet

MEAN = 90
VAR = 15
#APIタイムラインコール要求は最大 180 回 / 15 min 

def main():
    def stdout_clean():
        sys.stdout.write("\r                    \n")
        sys.stdout.flush()
    
    while True:
        sys.stdout.flush()
        idle_time = int(np.random.normal(MEAN, VAR))
        load_tweet.main()
#        display_tweet.main()

        t = 0
        while t < idle_time:
            sys.stdout.write("\r%d / %d" % (t, idle_time))
            sys.stdout.flush()
            time.sleep(1)
            t += 1

            if t == idle_time:
                stdout_clean()
    
if __name__ == '__main__':
    main()
