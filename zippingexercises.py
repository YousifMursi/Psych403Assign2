# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 09:26:12 2022

@author: yousi
"""

import numpy as np

first_item=[]
second_item=[]

img_F=['face1.png']*5+['face2.png']*5+['face3.png']*5+['face4.png']*5+['face5.png']*5
img_H=['houses1.png']*5+['houses2.png']*5+['houses3.png']*5+['houses4.png']*5+['houses5.png']*5

first_item.extend(img_F)
first_item.extend(img_H)
first_item.extend(img_F)
first_item.extend(img_H)
print(first_item)

image_FS=['face1.png', 'face2.png', 'face3.png', 'face4.png', 'face5.png']*5
image_HS=['houses1.png', 'houses2.png', 'houses3.png', 'houses4.png', 'houses5.png']*5

second_item.extend(image_HS)
second_item.extend(image_FS)
second_item.extend(image_HS)
second_item.extend(image_FS)
print(second_item)

cues=['cue1']*50+['cue2']*50

catimg=list(zip(first_item, second_item, cues))
print(catimg)

np.random.shuffle(catimg)
print(catimg)
