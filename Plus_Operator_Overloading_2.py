# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 08:31:24 2021

@author: Gourav
"""

class Distance:
    def __init__(self,foot=0,inch=0):
        self.foot = foot
        self.inch = inch
        
        
    def __add__(self,num):
        """Adding scalar value to a class """
        temp = self.foot * 12 + self.inch
        temp += num
        temp_obj = Distance()
        temp_obj.foot = temp // 12
        temp_obj.inch = temp % 12
        return temp_obj
    
    def __radd__(self,num):
        """Adding scalar value to a class reversly """
        temp = self.foot * 12 + self.inch
        temp += num
        temp_obj = Distance()
        temp_obj.foot = temp // 12
        temp_obj.inch = temp % 12
        return temp_obj
    
    
    
    def Display(self):
        print(f"The Distance is {self.foot} foot {self.inch} inches")
        
        
        
D1 = Distance(5,9)
D2 = D1 + 40
D2.Display()
D3 = 40+D1
D3.Display()