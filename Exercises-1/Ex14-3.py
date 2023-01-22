# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 14:38:11 2022

@author: Craig Murray
"""

string = '1 0 0 1 0 1'
 
binary = string[::2]
number = int(binary, 2)
 
 
print(f'Number found: {number}')
