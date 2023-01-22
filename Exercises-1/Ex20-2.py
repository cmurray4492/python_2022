# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 21:36:20 2022

@author: Craig Murray
"""
# check to see if last four end in '2020'

# code1 = 'FVNISJND-XX-2020'
# code2 = 'FVNISJND-XY-2019'

# cdm1 = code1[-4:]
# cdm2 = code2[-4:]
# # print(cdm1)
# # print(cdm2)

# craig1 = cdm1 == '2020'
# craig2 = cdm2 == '2020'

# print(f"code1: {craig1}")
# print(f"code2: {craig2}")

code1 = 'FVNISJND-XX-2020'
code2 = 'FVNISJND-XY-2019'
 
 
print(f"code1: {code1.endswith('2020')}")
print(f"code2: {code2.endswith('2020')}")