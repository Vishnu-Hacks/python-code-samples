# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 10:10:19 2018

@author: vishnu
"""

# pascalcase for classnames is recommended
class Profile : 
    
    """ All functions needs a self varibable as the first param in order
    to use the class variables """
    
    def __init__(self, name="not set",age = "unknown",courses=[]):
        """ constructor """
        self.name=name
        self.age=age
        self.courses=courses
        
    def displayProfile(self):
       print (self.name+ " : " + str(self.age))
       print("courses:")
       for x in self.courses:
           print x
       print("***********************")


profile1=Profile()
profile1.displayProfile()

profile2=Profile("Vishnu",21,["AI","ML"])
profile2.displayProfile()
       

