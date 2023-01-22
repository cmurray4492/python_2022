# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 14:34:51 2022

@author: Craig Murray
"""

string = 'PKV-89415-PLN'
 
code = string[:3] + string[-3:]
 
 
print(code)