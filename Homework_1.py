# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 14:26:22 2021

@author: Gourav
"""

class Student:
    student_list = []
    def __init__(self,roll,name,marks):
        self.roll = roll
        self.name = name
        self.marks = marks
        Student.student_list.append([roll,name,marks])
        
    @classmethod 
    def Display_Max(cls):
        cls.student_list.sort(key= lambda x:x[2], reverse=True)
        print(f"The Heighest Marks {cls.student_list[0][2]} was Scored by - {cls.student_list[0][1]}")
        
        
Person1 = Student(89,"Gourav Singh", 287)
Person2 = Student(88,"Gourav Singh 1", 281)
Person3 = Student(80,"Gourav Singh 2", 250)

Student.Display_Max()
