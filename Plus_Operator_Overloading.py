# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 08:24:12 2021

@author: Gourav
"""


"""
1) +     ==> __add__(self,object)
2) -     ==> __sub__(self,object)
3) *     ==> __mul__(self,object)
4) /     ==> __truediv__(self,object)
5) //     ==> __floordiv__(self,object)
6) %     ==> __mod__(self,object)
7) **     ==> __pow__(self,object)
8) >>     ==> __rshift__(self,object)
9) <<     ==> __lshift__(self,object)
10) &     ==> __and__(self,object)
11) |     ==> __or__(self,object)
12) ^     ==> __xor__(self,object)
13) <	  ==> __LT__(SELF, OTHER)
14) >     ==> __GT__(SELF, OTHER)
15) <=	  ==> __LE__(SELF, OTHER)
16) >=	  ==> __GE__(SELF, OTHER)
17) ==	  ==> __EQ__(SELF, OTHER)
18) !=	  ==> __NE__(SELF, OTHER)
19) -=	  ==> __ISUB__(SELF, OTHER)
20) +=	  ==>__IADD__(SELF, OTHER)
21) *=    ==> __IMUL__(SELF, OTHER)
22) /=	  ==> __IDIV__(SELF, OTHER)
23) //=	  ==> __IFLOORDIV__(SELF, OTHER)
24) %=	  ==> __IMOD__(SELF, OTHER)
25) **=	  ==> __IPOW__(SELF, OTHER)
26) >>=	  ==> __IRSHIFT__(SELF, OTHER)
27) <<=	  ==> __ILSHIFT__(SELF, OTHER)
28) &=	  ==> __IAND__(SELF, OTHER)
29) |=	  ==> __IOR__(SELF, OTHER)
30) ^=	  ==> __IXOR__(SELF, OTHER)
31) –	  ==>__NEG__(SELF, OTHER)
32) +	  ==> __POS__(SELF, OTHER)
33) ~	  ==> __INVERT__(SELF, OTHER)
34) in    ==> __contain__(self,other)
35) calling a class as function we use   ==> __call__(self,arguments)
36) representation   => __repr__(self)
"""
class comp:
    def __init__(self,real=0,img=0):
        self.real = real
        self.img = img
        
    def __add__(self,obj):
        """Overloading Addional Operator"""
        temp = comp()
        temp.real = self.real + obj.real
        temp.img = self.img + obj.img
        return temp
    
    
    def Display(self):
        print(f"{self.real} + i{self.img} ")
        
        
        
A1 = comp(5,6)
A2 = comp(2,4)

A3 = A1+A2
A3.Display()
        