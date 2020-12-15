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
	

# --- Part Two --- # 
"""
byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
	If cm, the number must be at least 150 and at most 193.
	If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not.
"""


def check_valid_data(passport: dict):
	"""
	Проверка корректности данных паспорта passport
	"""
	if all((
		1920 <= int(passport['byr']) <= 2002,
		2010 <= int(passport['iyr']) <= 2020,
		2020 <= int(passport['eyr']) <= 2030,
		(passport['hgt'][-2:] == 'cm' and 150 <= int(passport['hgt'][:-2]) <= 193 
			or passport['hgt'][-2:] == 'in' and 59 <= int(passport['hgt'][:-2]) <= 76),
		(passport['hcl'][0] == '#' and len(passport['hcl']) == 7),
		passport['ecl'] in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'), 
		(len(passport['pid']) == 9 and passport['pid'].isdigit()),
		)):
		return True
	return False


k_valid = 0
for u in data:
	if not set(required_fields).difference(set(u.keys())):
		if check_valid_data(u):
			k_valid += 1

print(f'part2. valid passports: {k_valid}')
