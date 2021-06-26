# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 11:48:33 2021

@author: Gourav
"""
# Hierarchical inheritance

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
        
class Semester_Marks(Student):
    def __init__(self,roll,name,sem_marks):
        Student.__init__(self,roll,name)
        self.sem_marks = sem_marks
        
    def Display(self):
        print(f"Roll = {self.roll} Name = {self.name} Semester Marks = {self.sem_marks}")
        
       
        
        
S1 = Internal_Marks(89,"Gourav",245)
S1.Display()

S2 = Semester_Marks(89,"Gourav",150)
S2.Display()