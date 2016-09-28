#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

import pytter.pytter as pytter

if __name__ == '__main__':
    argc = len(sys.argv)
    if argc < 2:
        exit()
    text = sys.argv[1]
    api = pytter.create_api()
    updated = api.update_status(text)

