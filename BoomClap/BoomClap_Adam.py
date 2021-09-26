# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 21:03:55 2021

@author: askle
"""

rules = {3:'Boom', 5:'Clap', 7:'Pop'}
for i in range(1,100):
    OUTPUT = ' '.join(word for num, word in rules.items() if i%num==0)
    print(OUTPUT if OUTPUT else i)
