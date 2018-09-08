# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 11:02:42 2018

@author: vishn
"""

""" zip function combines the correspoding elements of the two lists into tuples
the function terminates when the tuple pairs becomes the size of the smallest array,
in the following scenario 'd' will not be used to form any tuples """
list1=[1,2,3]
list2=['a','b','c','d']

tuples=zip(list1,list2)

print tuples