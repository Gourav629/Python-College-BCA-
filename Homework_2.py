# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 15:51:01 2021

@author: Gourav
"""

class Student:
    student_list = []
    roll = 0
    def __init__(self,name,cp,java,python):
        self.name = name
        self._marks_cplusplus = float(cp)
        self._marks_java = float(java)
        self._marks_python = float(python)
        Student.roll+=1
        Student.student_list.append([Student.roll,name,self._marks_cplusplus+self._marks_java+self._marks_python])
     
        
    def Display(self):
        print(f"Name : {self.name} Marks in Python = {self._marks_python}  C++ = {self._marks_cplusplus}  Java = {self._marks_java}")
        
    @classmethod 
    def Display_Max(cls):
        cls.student_list.sort(key= lambda x:x[2], reverse=True)
        print(cls.student_list[0][0])
        print(f"The Highest Marks {cls.student_list[0][2]} was Scored by - {cls.student_list[0][1]} ")
        
        
        
Person1 = Student("Gourav Singh", 98,77,100)
Person1.Display()
Person2 = Student("Gourav Singh 1",98,77,70)
Person3 = Student("Gourav Singh 2",98,77,56)

Student.Display_Max()