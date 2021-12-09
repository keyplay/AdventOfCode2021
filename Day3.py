# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 17:10:37 2021

@author: NTU
"""



with open('Day3_input.txt', 'r') as f:
    data = f.readlines()

bit_cnt = [0] * 12
for ele in data:
    for i in range(12):
        if ele[i] == '1':
            bit_cnt[i] += 1

bit_common = ['0'] * 12
for i in range(12):
    if bit_cnt[i] > len(data)/2:
        bit_common[i] = '1'

result = ''        
for ele in bit_common:
    result += ele
result = int(result, 2)