#!/usr/bin/env/python
#-*- coding:utf-8 -*-
__author__ = 'tim'

from PyQt5.QtCore import QObject, pyqtSignal


class Foo(QObject):
    trigger=pyqtSignal()

    def connect_and_emit_trigger(self):
        self.trigger.connect(self.handle_trigger)
        self.trigger.emit()

    def handle_trigger(self):
        print "Trigger signal received"

foo=Foo()
foo.connect_and_emit_trigger()
