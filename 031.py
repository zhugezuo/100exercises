#!/usr/bin/python
# -*- coding: UTF-8 -*-
s1 = raw_input("Please enter the first letter: \n")
if s1 =='S':
    s2 = raw_input ("Please enter the second letter:")
    if s2 == 'a':
        print("Saturday")
    elif s2 == 'u':
        print("Sunday")
    else:
        print("Error")
elif s1 == 'T':
    s2 = raw_input ("Please enter the second letter:")
    if s2 == 'u':
        print("Tuesday")
    elif s2 == 'h':
        print("Thursday")
    else:
        print("Error")
elif s1 == 'M':
    print("Monday")
elif s1 == 'W':
    print("Wednesday")
elif s1 == 'F':
    print("Friday")
