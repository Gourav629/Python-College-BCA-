# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 09:01:21 2021

@author: Gourav
"""

def Divs(num,z):
    try:
        r = num / z
        print(r)
    except (ZeroDivisionError) :
        print("Cannot Divid By Zero")
        
        
Divs(5,2)
Divs(5,0)
        
    