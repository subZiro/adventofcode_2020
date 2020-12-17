# -*- coding: utf-8 -*-
# --- Day 6: Custom Customs --- # 

from collections import Counter


def get_data():
	"""
	Получение списка групп и ответов да на вопросы
	"""
	result = []
	one_user = []
	f = open('../data/day_6.txt', 'r')
	for line in f:
		if line.rstrip():
			one_user.append(line.rstrip())
		else:
			result.append(one_user)
			one_user = []
	result.append(one_user)    # last user group
	return result

answer_is_yes = ['a', 'b', 'c', 'x', 'y', 'z']


# --- Part One --- #
"""
abc

a
b
c

ab
ac

a
a
a
a

b

This list represents answers from five groups:
	The first group contains one person who answered "yes" to 3 questions: a, b, and c.
	The second group contains three people; combined, they answered "yes" to 3 questions: a, b, and c.
	The third group contains two people; combined, they answered "yes" to 3 questions: a, b, and c.
	The fourth group contains four people; combined, they answered "yes" to only 1 question, a.
	The last group contains one person who answered "yes" to only 1 question, b.
	In this example, the sum of these counts is 3 + 3 + 3 + 1 + 1 = 11.
"""

answer_groups = get_data()
result = []
for group in answer_groups:
	ans = []
	for answer in group:
		ans.extend([a for a in answer])
	result.extend(list(set(ans)))
print(f'those counts part 1: {len(result)}')
