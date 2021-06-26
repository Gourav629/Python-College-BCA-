# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 08:47:47 2021

@author: Gourav
"""
"""
Not Implemented Error ===> Abstract class
"""
class Sample:
    
    def __init__(self,m1,m2,m3):
        self.marks = {'C':m1,'C++':m2,'Java':m3}
        
    def __contains__(self,subject):
        """Overloading in Operator """
        if subject in self.marks:
            return True
        else:
            return False
    
    def __call__(self,name):
        """Calling function"""
        print(f"Hi !!! {name}")
    
    
    
S1 = Sample(25,45,60)
print("Python" in S1)
print("Java" in S1)
print("java" in S1)
S1("Gourav")