#!/usr/bin/python
# -*- coding: UTF-8 -*-
import string

s = raw_input('input a string:\n')
letters = 0
space = 0
digit = 0
others = 0
for c in s:
    if c.isalpha():
        letters += 1
    elif c.isdigit():
        digit += 1
    elif c.isspace():
        space += 1
    else:
        others += 1
print ("letters:%2d\n") % letters
print ("digit:  %2d\n") % digit
print ("space:  %2d\n") % space
print ("others: %2d\n") % others
