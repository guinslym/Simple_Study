#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import zipfile
import datetime

def print_info(archieve_name):
    with zipfile.ZipFile(archieve_name) as zf:
        for info in zf.infolist():
            print info.filename
            print "\tComment:",info.comment
            mod_date=datetime.datetime(*info.date_time)
            print "\tModified:",mod_date
            if info.create_system==0:
                system="Windows"
            elif info.create_system==3:
                system="Unix"
            else:
                system="UnKnown"
            print "\tSystem:",system
            print "\tZip Version:",info.create_version
            print "\tCompressed:",info.compress_size,"bytes"
            print "\tUncompressed",info.file_size,"bytes"
            print "-"*30

if __name__ == "__main__":
    print_info("test.zip")