#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 22:52:03 2020

@author: carlyfabris
"""

keep_going = 'y'
starting_number = 0
while keep_going == 'y':
    new_number = int(input("How many numbers would you like to print? "))
    for x in range(starting_number, starting_number + new_number):
        print (x)
        starting_number = x +1
    keep_going = input("Would you like to keep going? [y]es or [n]o: ")


print("Thanks for playing!")

