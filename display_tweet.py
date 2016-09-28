#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd

BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'

EMPTY_NUM = 5

if __name__ == '__main__':
    df = pd.read_csv('.tweet_bash_v001.csv')
    for i,row in df.iterrows():
        text = row['text']
        author_name = row['author_name']

        print GREEN + '(' +  author_name + ')' + YELLOW + '-> ' + ENDC
        print (' '*EMPTY_NUM) + text
    
