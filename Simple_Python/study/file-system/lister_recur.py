#!/usr/bin/env/python

from __future__ import print_function
import os,sys

def lister_recur(directory):
    print('-'*10+directory+'-'*10)
    for file in os.listdir(directory):
        path = os.path.join(directory,file)
        if not os.path.isdir(path):
            print(path)
        else:
            lister_recur(path)

if __name__ == '__main__':
    lister_recur(sys.argv[1])