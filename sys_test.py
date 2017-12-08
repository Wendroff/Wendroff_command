# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 14:36:43 2017

@author: wendroff
"""

import sys
#print(len(sys.argv))
hello = open('hello.dat','w')
for thing in sys.argv :
    print(thing)
    hello.write(thing+'\n')

name = input("Please input your name:\n")

hello.write("Hello "+name+'\n')
print("Hello,", name)

hello.close()