# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 11:29:52 2021

@author: Gourav
"""

# Single Inheritance


class Student:
    def __init__(self, roll, name):
        self.roll = roll
        self.name = name
        
    def Display(self):
        print("Inside Student")
        
class Internal_Marks(Student):
    def __init__(self, roll, name, imarks):
        Student.__init__(self,roll,name)
        self.imarks = imarks
        
    def Display(self):
        print(f"Roll = {self.roll} Name = {self.name} Internal Marks = {self.imarks}")
        
        
        
        
S = Internal_Marks(89,"Gourav",245)
S.Display()
