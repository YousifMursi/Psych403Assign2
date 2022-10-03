# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 09:15:46 2022

@author: yousi
"""

colors=['red','orange','yellow','green','blue','purple']

print(colors[4])
print(colors[4][-2])
print(colors[4][-1])

colors.remove('purple')
colors.insert(5, 'indigo')
colors.insert(6,'violet')
print(colors)
