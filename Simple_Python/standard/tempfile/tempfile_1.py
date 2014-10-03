import os
import tempfile

data="""this is something test examlpe about tempfile module.
and it can be use fast.
what you say it is?
so you sneek
my site you can link
"""

def make_tempfile():
    fd,temp_file_name=tempfile.mkstemp()
    os.close(fd)
    f=open(temp_file_name,"wt")
    try:
        f.write(data)
    finally:
        f.close()
    return temp_file_name
def cleanup(filename):
    os.unlink(filename)
