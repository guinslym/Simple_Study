__author__ = 'Dog'

import os
import os.path
root_dir = "f:/mysite"
for parent, dir_names, file_names in os.walk(root_dir):
    for dir_name in dir_names:
        print "parent is: " + parent
        print "dirname is: " + dir_name
    for file_name in file_names:
        print("parent is: " + parent)
        print("filename with full path: " + os.path.join(parent,file_name))