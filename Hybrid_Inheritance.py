# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 12:18:03 2021

@author: Gourav
"""

# Hybrid Inheritance


class Student:
    def __init__(self,roll, name):
        self.roll = roll
        self.name = name
        
    def Display(self):
        print("Inside Student Class ")
    
    
class Internal(Student):
    def __init__(self,roll, name,imarks):
        Student.__init__(self,roll,name)
        self.imarks = imarks
    
    def Display(self):
        print("Inside Internal Class")


class External(Student):
    def __init__(self,roll, name,sem_marks):
        Student.__init__(self,roll,name)
        self.sem_marks = sem_marks
    
    def Display(self):
        print("Inside External Class")


class Marksheet(External,Internal):
    def __init__(self,roll,name,imarks,sem_marks):
        Internal.__init__(self,roll,name,imarks)
        External.__init__(self,roll,name,sem_marks)
        self.total = float(imarks) + float(sem_marks)
        
    
    def Total_Display(self):
        print(f"Roll = {self.roll} Name = {self.name} Semester Marks = {self.sem_marks} Internal Marks = {self.imarks} Total Marks = {self.total}")
    
    def Simple(self):
        self.Display()

S2 = Marksheet(89,"Gourav",250,150)
S2.Total_Display()
S2.Simple()





