#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 22:52:03 2020

@author: carlyfabris
"""

keep_going = 'y'

numbers = int(input("How many numbers would you like to print? "))
while keep_going == 'y':
    for x in range(0, numbers):
        print (x)
        a = int(x)
    keep_going = input("Would you like to keep going? [y]es or [n]o: ")
    if keep_going == 'y':
        numbers = int(input(("How many numbers would you like to print? ")))     
        pass
    else:
        break
    while numbers > 0:
        a += 1
        print (a)
        numbers -= 1

print("Thanks for playing!")

