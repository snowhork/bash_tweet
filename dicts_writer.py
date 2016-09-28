#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import csv

class dicts_writer:
    
    def __init__(self, csv_path):
        self.rows = []
        self.csv_base_name = '.tweet_bash'
        self.version = 'v001'
        self.csv_path = csv_path
        self.csv_name = self.csv_base_name + '_' + self.version + '.csv'

        self.file = open(os.path.join(self.csv_path, self.csv_name), 'w')
        self.writer = csv.writer(self.file)
        
    def write_header(self, row):
        self.writer.writerow(row.keys())

    def write_row(self, row):
        self.writer.writerow(row.values())
        
    def write_rows(self, rows):
        write_header_flag = True
        for row in rows:
            if write_header_flag:
                self.write_header(row)
                write_header_flag = False
            self.write_row(row)
        
    def close(self):
        self.file.close()

