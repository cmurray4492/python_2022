# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 21:54:38 2022

@author: Craig
"""

pv = 1000 
ira = 1.03
i_period = 5

for i in range(i_period):
    pv *= ira
    
# fv = "{:.2f}".format(pv)
fv = pv

print(f"The future value of the investment: {fv} USD ")

print(f'The future value of the investment: {fv:.2f} USD')
