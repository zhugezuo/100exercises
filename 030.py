#!/usr/bin/python
# -*- coding: UTF-8 -*-
def reverse(s, l):
    t = []
    for i in range(l):
        t.append(s[l - i - 1])
    return t


def to_str(n):
    t = []
    for c in n:
        t.append(c)
    return t


s = raw_input("s:")
r = reverse(s, len(s))
if to_str(s) == r:
    print ("是回文数")
else:
    print ("不是回文数")
