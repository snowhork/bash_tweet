#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd

BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'

INDENT_NUM = 5

def indent():
    return ' '*INDENT_NUM

def main():
    df = pd.read_csv('.tweet_bash_v001.csv')
    for i,row in df.sort(ascending=False).iterrows():
        text = row['text'].replace('\n', '\n'+indent())
        author_name = row['author_name']

        print GREEN + '(' +  author_name + ')' + YELLOW + '-> ' + ENDC
        print indent() + text
    
if __name__ == '__main__':
    main()
