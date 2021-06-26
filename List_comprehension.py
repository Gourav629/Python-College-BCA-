# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 11:46:52 2021

@author: Gourav
"""

"""
list = [expression for var in sequence if condition ]

Note : 
    1) if the condition has any else part it(Condition) should be written at the 
left side of the iteration. 
    2) if there is no else condition then the condition would be in right side
    3) for nested if it also should be written in right
"""

Squares = [i**2 for i in range(1,11)]
Squares

nums = [1,2,3,4,5,6,7,8,9,10]
odds = [i if i%2!=0 else 0 for i in nums]
odds