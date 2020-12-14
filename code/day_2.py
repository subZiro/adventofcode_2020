# -*- coding: utf-8 -*-
#--- Day 2: Password Philosophy ---#
#--- День 2: Философия паролей ---#


import re
f = open('../data/day_2.txt', 'r')
arr_0 = ['1-3 a: abcde', '1-3 b: cdefg', '2-9 c: ccccccccc']


#--- Part One ---#
"""
Each line gives the password policy and then the password. 
The password policy indicates the lowest and highest number of times 
a given letter must appear for the password to be valid. For example, 
1-3 a means that the password must contain a at least 1 time and at most 3 times.

In the above example, 2 passwords are valid. 
The middle password, cdefg, is not; it contains no instances of b, but needs at least 1. 
The first and third passwords are valid: they contain one a or nine c, 
both within the limits of their respective policies.

1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
"""
total_1 = 0
for line in f:
	i, k, text = line.split(' ')
	i = i.split('-')
	if int(i[0]) <= text.count(k[:-1]) <= int(i[1]):
		total_1 += 1
print(f'part one result: {total_1}')


#--- Part Two ---#
"""
Given the same example list from above:

1-3 a: abcde is valid: position 1 contains a and position 3 does not.
1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.
"""
total_2 = 0
for line in f:
	i, k, text = line.split(' ')
	i = i.split('-')
	k = k[:-1]§
	pos1 = int(k == text[int(i[0])-1])
	pos2 = int(k == text[int(i[1])-1])
	print(pos1, pos2)
	if pos1 + pos2 == 1:
		total_2 += 1
print(f'part one result: {total_2}')
