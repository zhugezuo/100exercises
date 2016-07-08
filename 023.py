#!/usr/bin/python
# -*- coding: UTF-8 -*-
from sys import stdout

for i in range(4):
    for j in range(3 - i):
        stdout.write(" ")
    for j in range(2 * i + 1):
        stdout.write("*")
    stdout.write("\n")

for i in range(3):
    for j in range(i + 1):
        stdout.write(" ")
    for j in range(5 - 2 * i):
        stdout.write("*")
    stdout.write("\n")
