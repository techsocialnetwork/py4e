# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 15:36:13 2021

@author: lofth
"""

num = 0
tot = 0.0
while True:
    sval = input('Enter a number: ')
    if sval == 'done':
        break
    try:
        fval = float(sval)
    except:
        print('invalid input')
        continue
        #print(fval)
    num = num + 1
    tot = tot + fval
    
#print('ALL DONE')
print(tot,num,tot/num)

    