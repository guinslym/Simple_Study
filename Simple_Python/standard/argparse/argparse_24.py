#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import argparse

class CustomAction(argparse.Action):
    def __init__(self,
                      option_strings,
                      dest,
                      nargs=None,
                      const=None,
                      default=None,
                      type=None,
                      choices=None,
                      required=None,
                      help=None,
                      metavar=None):
        argparse.Action.__init__(self,
                                              option_strings=option_strings,
                                              dest=dest,
                                              nargs=nargs,
                                              const=const,
                                              default=default,
                                              type=type,
                                              choices=choices,
                                              required=required,
                                              help=help,
                                              metavar=metavar
                                              )
        print 'Initializing CustomAction'
        for name,value in sorted(locals().items()):
            if name == 'self' or value is None:
                continue
            print ' %s = % r' % (name,value)
        print
        return
    def __call__(self,parser,namespace,values,
                      option_strings=None):
        print 'Processing CustomAction for "%s"' % self.dest
        print ' parser = %s' % id(parser)
        print ' values = %r' % values
        print ' option_strings = %r' % option_strings

        # Do some arbitrary processing of the input values
        if isinstance(values,list):
            values = [v.upper() for v in values]
        else:
            values = values.upper()

        # Save the results in the namespace using the destination
        # variable given to our constructor.
        setattr(namespace,self.dest,values)
        print

parser = argparse.ArgumentParser()
parser.add_argument('-a',action=CustomAction)
parser.add_argument('-m',nargs='*',action=CustomAction)
results = parser.parse_args(['-a','values',
                                             '-m','multivalue',
                                             'second'])
print results