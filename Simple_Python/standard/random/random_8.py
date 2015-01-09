#! /us/bin/env/python
# -*- coding:utf-8 -*-

import random
import itertools

FACE_CARDS = ('J','Q','K','A')
SULTS = ('H','D','C','S')

def new_desk():
    return list(itertools.product(
    	itertools.chain(xrange(2,11),FACE_CARDS),
    	SULTS,
    	))

def show_desk(desk):
    p_desk = desk[:]
    while p_desk:
    	row = p_desk[:13]
    	p_desk = p_desk[13:]
    	for j in row:
    	    print '%2s%s' % j,
    	print

#Make a new deck,with the cards in order
desk = new_desk()
print 'Initial deck:'
show_desk(desk)

#Shuffle the deck to randomize the order
random.shuffle(desk)
print '\nShuffled desk:'
show_desk(desk)

#Deal 4 hands of 5 cards
hands = [ [],[],[],[]]
for i in xrange(5):
    for h in hands:
    	h.append(desk.pop())

# Show the hands
print '\nHands'
for n,h in enumerate(hands):
    print '%d:' % (n+1)
    for c in h:
        print '%2s%s' % c,
    print

#Show the ramaining desk
print '\nRemaining desk'
show_desk(desk)