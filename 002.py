#!/usr/bin/python
# -*- coding: UTF-8 -*-
r=0
i = int(raw_input('请输入当月利润:'))
if i<100000:
    r=0.1*i
elif (i>=100000 and i<200000):
    r=10000+0.075*(i-100000)
elif (i>=200000 and i<400000):
    r=17500+0.05*(i-200000)
elif (i>=400000 and i<600000):
    r=27500+0.03*(i-400000)
elif (i>=600000 and i<1000000):
    r=33500+0.015*(i-600000)
elif i>=1000000:
    r=39500+0.01*(i-1000000)
print r

r=0
arr = [1000000,600000,400000,200000,100000,0]
rat = [0.01,0.015,0.03,0.05,0.075,0.1]
for idx in range(0,6):
    if i>arr[idx]:
        r=r+(i-arr[idx])*rat[idx]
        i=arr[idx]
print r