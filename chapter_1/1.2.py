import unittest
from collections import Counter


def check_permutation(string_one, string_two):
	if len(string_one) != len(string_two):
		return False
	for character in string_one:
		if string_one.count(character) != string_two.count(character):
			return False
	return True


def check_permutation_with_counter(string_one, string_two):
	if len(string_one) != len(string_two):
		return False
	counter_one = Counter(string_one)
	counter_two = Counter(string_two)
	for character in string_one:
		if counter_one[character] != counter_two[character]:
			return False
	return True


class TestCase(unittest.TestCase):
	dataTrue = (('abcd', 'bacd'), ('3563476', '7334566'), ('wef34f', 'wffe34'))
	dataFalse = (('abcd', 'd2cba'), ('2354', '1234'), ('dcw4f', 'dcw5f'))

	def test_check_permuation(self):
		for strings in self.dataTrue:
			result = check_permutation(*strings)
			self.assertTrue(result)
		for strings in self.dataFalse:
			result = check_permutation(*strings)
			self.assertFalse(result)

	def test_check_permutation_with_counter(self):
		for strings in self.dataTrue:
			result = check_permutation_with_counter(*strings)
			self.assertTrue(result)
		for strings in self.dataFalse:
			result = check_permutation_with_counter(*strings)
			self.assertFalse(result)


unittest.main()
