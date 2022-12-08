# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 12:09:45 2022

@author: Ashutosh Verma
"""

def even_check(n):
    if n%2 ==0:
        print("number is even")
    else :
        print("number is odd")
        
def factor(n):
    temp =[]
    for i in range(1,n):
        if n%i==0:
            temp.append(i)
        return temp
    print(*temp)


