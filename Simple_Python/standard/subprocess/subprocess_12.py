#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import subprocess

cat = subprocess.Popen(['cat','webservice'],
                                    stdout=subprocess.PIPE,
                                    )
grep = subprocess.Popen(['grep','..include::'],
                                    stdin=cat.stdout,
                                    stdout=subprocess.PIPE,
                                   )
cut = subprocess.Popen(['cut','-f','3','-d:'],
                                    stdin=grep.stdout,
                                    stdout=subprocess.PIPE,
                                  )

end_of_pipe = cut.stdout
print 'Included files:'
for line in end_of_pipe:
    print '\t',line.strip()