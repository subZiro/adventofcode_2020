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


# --- Part Two --- #
"""
This list represents answers from five groups:
	In the first group, everyone (all 1 person) answered "yes" to 3 questions: a, b, and c.
	In the second group, there is no question to which everyone answered "yes".
	In the third group, everyone answered yes to only 1 question, a. 
		Since some people did not answer "yes" to b or c, they don't count.
	In the fourth group, everyone answered yes to only 1 question, a.
	In the fifth group, everyone (all 1 person) answered "yes" to 1 question, b.
	In this example, the sum of these counts is 3 + 0 + 1 + 1 + 1 = 6.
"""

result = []
for group in answer_groups:
	count_user = len(group)
	answ_counts = Counter("".join(group))
	count = Counter(list(answ_counts.values()))[count_user]
	result.append(count)
print(f'those counts part 2: {sum(result)}')
