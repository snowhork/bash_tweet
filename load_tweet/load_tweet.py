#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import pickle

import dicts_writer
import pytter.pytter as pytter
import display_tweet.display_tweet as display

def pkl_name(id):
    return str(id) + '.pickle'

def main():
    api = pytter.create_api()
    timeline = api.home_timeline()

    pkl_output = 'status_pickles/'
    
    for status in timeline:
        id = status.id

        pkl_path = os.path.join(pkl_output, pkl_name(id))
        if not os.path.exists(pkl_path):
            with open(pkl_path, mode='wb') as f:
                pickle.dump(status, f)
            display.display_status(status)

if __name__ == '__main__':
#    argc = len(sys.argv)
#    if argc < 2:
#        exit()
#    text = sys.argv[1]
    main()
