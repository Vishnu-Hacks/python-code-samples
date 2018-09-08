# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 11:11:47 2018

@author: vishn
"""

""" function with arbitary number of arguments """

def  myFunction(*arguments,**keyvalueArguments):
    """ this function takes any num of arguments and any number of key&value pair
    arguments """
    print arguments
    print keyvalueArguments
    
def myFunction2(*args):
    """ only takes any number of arguments no key&value pairs"""
    print args
    

myFunction('a','b',name="vishnu")
#('a', 'b')
#{'name': 'vishnu'}


myFunction2('a','b')
#('a', 'b')