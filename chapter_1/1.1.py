def is_unique(string):
    compare = ''
    for s in string:
        if s not in compare:
            compare = compare + s
        else:
            return False
    return True

print(is_unique('asdfghjk'))