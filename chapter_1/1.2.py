def check_if_permutation(string_one, string_two):
	for character in string_one:
		if string_one.count(character) == string_two.count(character):
			pass
		else:
			return False
	return True

string1 = 'abcdefg'
string2 = 'gfedcba'
string3 = 'agfgaerggearg'

print(check_if_permutation(string1, string2)) # Should return True
print(check_if_permutation(string1, string3)) # Should return False