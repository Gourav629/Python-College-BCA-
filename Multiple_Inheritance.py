# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 11:58:17 2021

@author: Gourav
"""

# Multiple Inheritance
        
class Internal_Marks(object):
    def __init__(self, imarks,smarks):
        super(Internal_Marks,self).__init__(smarks)
        self.imarks = imarks
   
class Semester_Marks:
    def __init__(self,sem_marks):
        self.sem_marks = sem_marks
        
class Student(Internal_Marks,Semester_Marks):
    def __init__(self, roll, name,imarks,sem_marks):
        super(Student,self).__init__(imarks,sem_marks)
        self.roll = roll
        self.name = name
        
    def Display(self):
        print(f"Roll = {self.roll} Name = {self.name} Semester Marks = {self.sem_marks} Internal Marks = {self.imarks}")
           
       

S2 = Student(89,"Gourav",250,150)
S2.Display()


# By Name Constructor Call


class Internal_Marks(object):
    def __init__(self, imarks):
        self.imarks = imarks
   
class Semester_Marks:
    def __init__(self,sem_marks):
        self.sem_marks = sem_marks
        
class Student(Internal_Marks,Semester_Marks):
    def __init__(self, roll, name,imarks,sem_marks):
        Internal_Marks.__init__(self,imarks)
        Semester_Marks.__init__(self,sem_marks)
        self.roll = roll
        self.name = name
        
    def Display(self):
        print(f"Roll = {self.roll} Name = {self.name} Semester Marks = {self.sem_marks} Internal Marks = {self.imarks}")
           
       

S2 = Student(89,"Gourav",250,150)
S2.Display()






