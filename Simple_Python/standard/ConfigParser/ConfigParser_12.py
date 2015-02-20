#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import ConfigParser

# Define the names of the options
option_names = [
      'from-default',
      'from-section',
      'file-only',
      'init-only','init-and-file',
      'from-vars',
      ]
# Initialize the parser with some defaults
parser = ConfigParser.SafeConfigParser(
    defaults={
              'from-default':'value from defaults passed to init',
              'init-only':'value from defaults passed to init',
              'init-and-file':'value from defaults passed to init',
              'from-section':'value from defaults passed to init',
              'from-vars':'value from defaults passed to init',
    })
print 'Defaults before loading file:'
defaults = parser.defaults()
for name in option_names:
    if name in defaults:
        print ' %-15s = %r' % (name,defaults[name])

# Load the configuration file
parser.read('with-defaults.ini')
print '\nDefaults after loading file:'
for name in option_names:
    if name in defaults:
        print '%-15s = %r' % (name,defaults[name])
# Define some local overrides
vars = {'from-var':'value from vars'}
# Show the values of all the options
print '\nOption lookup'
for name in option_names:
    value = parser.get('sect',name,vars=vars)
    print '%-15s=%r' % (name,value)
# Show error messages for options that do not exist
print '\nError cases:'
try:
    print 'No such option:',parser.get('sect','no-option')
except ConfigParser.NoOptionError, err:
    print str(err)

try:
    print 'No such section:',parser.get('no-sect','no-option')
except ConfigParser.NoSectionError, err:
    print str(err)