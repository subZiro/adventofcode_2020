# -*- coding: utf-8 -*-


# --- Day 4: Passport Processing --- #
# --- Part One --- #
"""
The automatic passport scanners are slow because they're having trouble detecting 
which passports have all required fields. The expected fields are as follows:
	byr (Birth Year)
	iyr (Issue Year)
	eyr (Expiration Year)
	hgt (Height)
	hcl (Hair Color)
	ecl (Eye Color)
	pid (Passport ID)
	cid (Country ID)
"""


def get_data():
	"""
	Получение данных по пользователям
	"""
	f = open('../data/day_4.txt', 'r')
	result = []

	one_user = {}
	for line in f:
		data_line = {kv[:3]: kv[4:] for kv in line.split()}
		if data_line:
			one_user.update(data_line)
		else:
			result.append(one_user)
			one_user = {}
	result.append(one_user)	 # last user data
	return result


required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
data = get_data()
k_valid = 0
for u in data:
	if not set(required_fields).difference(set(u.keys())):
		k_valid += 1

print(f'part1. valid passports = {k_valid}')
