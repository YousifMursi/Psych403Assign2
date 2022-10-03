# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 15:08:01 2022

@author: yousi
"""

#List Operations Exercises

import numpy as np

numlist=[1,2,3]
print(numlist*2)

numarr=np.array([1,2,3])
print(numarr*2)

strlist=["do","re","mi","fa"]

#3a
print(strlist[0]*2,
      strlist[1]*2,
      strlist[2]*2,
      strlist[3]*2)
#3b
print(strlist*2)

#3c
print([strlist[0],strlist[0],
      strlist[1],strlist[1],
      strlist[2],strlist[2],
      strlist[3],strlist[3]])


#3d
print([[strlist[0],strlist[0]],
      [strlist[1],strlist[1]],
      [strlist[2],strlist[2]],
      [strlist[3],strlist[3]]])




