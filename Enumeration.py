# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 10:36:26 2018

@author: vishn
"""

""" Enumerations is mainly used when iterating over list and using both
the index and the element """
list1=[x for x in range(100,112)]

#pythonic way
for index,doc in enumerate(list1):
    print(str(index)+" : "+str(doc))
    
""" This can be also achieved using many other ways other pythonic way, 
  like the one below """
  
print "................"


#not pythonic way
for i in range(len(list1)):
    print(str(i)+" : "+str(list1[i]))