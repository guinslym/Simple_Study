#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import abc
from abc_1 import PluginBase

class LocalBaseClass(object):
    pass

class RegisteredImplementation(LocalBaseClass):
    def load(self,input):
        return input.read()
    def save(self,output,data):
        return output.write(data)
PluginBase.register(RegisteredImplementation)
if __name__ == '__main__':
    print 'Subclass:',issubclass(RegisteredImplementation,
                                              PluginBase)
    print 'Instance:',isinstance(RegisteredImplementation(),
                                             PluginBase)