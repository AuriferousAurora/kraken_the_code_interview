import unittest

def is_unique(string):
    compare = ''
    for s in string:
        if s not in compare:
            compare = compare + s
        else:
            return False
    return True

class TestCase(unittest.TestCase):

    dataTrue = ('abcdefghijkl', 's123vdefg', 'incoretal')
    dataFalse = ('gfdsagadsgffdsf', '1212121234221', 'dfde34dccsadfbbb')

    def test_is_unique(self):
        for string in self.dataTrue:
            result = is_unique(string)
            self.assertTrue(result)
        for string in self.dataFalse:
            result = is_unique(string)
            self.assertFalse(result)


unittest.main()
