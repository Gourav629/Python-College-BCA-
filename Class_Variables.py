# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 19:54:01 2021

@author: Gourav
"""

class sample:
    z = 0                 #class variable
    def __init__(self,a=0,b=0):
        self.x = a        #instance variable
        self.y = b
        sample.z += 1
        
    def display(self):
        print(f"A = {self.x} , B = {self.y} , Z = {sample.z}")
        
    def __setitem__(self):
        
        
    def __del__(self):
        sample.z-=1
        print(f"Object Destroyed when {sample.z} ")
        
        
        
s1 = sample()
s1.display()

s2 = sample(10,20)
s2.display()

del(s1)
del(s2)