# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 19:51:07 2021

@author: Gourav
"""

class sample:
    z = 0                 #class variable
    def __init__(self,a=0,b=0):
        self.x = a        #instance variable
        self.y = b
        self.__p = 10
        sample.z += 1
    def display(self):
        print(f"A = {self.x} , B = {self.y} , Z = {sample.z}  P = {self.__p}")
      
    @staticmethod
    def check():
        print("Checking by Removing Self")
        
    def __setitem__(self,g):
        self.g = g
        
    def __del__(self):
        sample.z-=1
        print(f"Object Destroyed when {sample.z} ")
        
        
        
s1 = sample()
s1.display()
s1.gourav = "Gourav"
s2 = sample(10,20)
s2.display()
s3 = sample(1,2)
s3.__setitem__("Gourav Singh")
print(s3.g)
print(s1.gourav)
print(s1.x)

setattr(s2,"name","S2")
print(s2.name)
print("\\\\\\\\\\\\\\")
s1.check()