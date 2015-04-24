#!/usr/bin/env/python

from __future__ import print_function
import os,sys

def lister(directory,suffix=None):
    '''A function for list all files in given directory'''
    for (thisdir,subdir,fileshere) in os.walk(directory):
        print('-'*10+thisdir+'-'*10)
        for fname in fileshere:
            if suffix is not None:
                if fname.endswith(suffix):
                    path = os.path.join(thisdir,fname)
                    print(path)
                else:
                    continue
            else:
                path = os.path.join(thisdir,fname)
                print(path)

if __name__ == '__main__':
    arg_len = len(sys.argv)
    if arg_len==2:
        lister(sys.argv[1])
    elif(arg_len==3):
        lister(sys.argv[1],sys.argv[2])
    else:
        print('Please input the directory where you want to search')