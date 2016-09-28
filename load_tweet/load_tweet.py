#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import dicts_writer

import pytter.pytter as pytter

def main():
    api = pytter.create_api()
    timeline = api.home_timeline()

    writer = dicts_writer.dicts_writer('.')
    rows = []
    
    for status in timeline:
        row = {}
        row['text'] = status.text.encode('utf-8')
        row['author_name'] = status.author.name.encode('utf-8')
        row['created_at'] = status.created_at
        rows.append(row)

    writer.write_rows(rows)    

if __name__ == '__main__':
#    argc = len(sys.argv)
#    if argc < 2:
#        exit()
#    text = sys.argv[1]
    main()
