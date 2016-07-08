#!/usr/bin/python
# -*- coding: UTF-8 -*-

def isLeapYear(iYear):
    if (iYear % 4 != 0) or (iYear % 100 == 0 and iYear % 400 != 0):
        return 0
    else:
        return 1


iMonth = [[0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31], [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]]
year = int(raw_input('year:\n'))
month = int(raw_input('month:\n'))
if month < 1 or month > 12:
    print "输入错误！"
else:
    day = int(raw_input('day:\n'))
    if day < 1 or day > iMonth[isLeapYear(year)][month]:
        print "输入错误！"
    else:
        total = 0
        for x in range(month):
            total += iMonth[isLeapYear(year)][x]
        print total + day

months = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)
if 0 < month <= 12:
    s = months[month - 1]
else:
    print 'data error'
s += day
leap = 0
if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    leap = 1
if (leap == 1) and (month > 2):
    s += 1
print 'it is the %dth day.' % s
