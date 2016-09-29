#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import pickle

BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'

INDENT_NUM = 5

def process_text(text):
    return text.replace('\n', '\n'+indent())

def display_status(status):
    text = process_text(status.text)
    author_name = status.author.name

    print GREEN + '(' +  author_name + ')' + YELLOW + '-> ' + ENDC
    print indent() + text

def display_pkl(pkl_path):
    with open(pkl_path, mode='rb') as f:
        status = pickle.path(f)
    display_status(status)
        
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
