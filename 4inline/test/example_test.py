import unittest
from fourinlineclass import FourInLine

class FourInLineTest(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
    def test_fourHorizontal(self):
        f = FourInLine()
        for i in range(1,4):
            f.dropChip(i)
        r = f.dropChip(4)
        self.assertEqual(f.check4Horizontal(r[0],r[1]), True)


if __name__ == '__main__':
    unittest.main()
