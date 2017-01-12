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
        p = f.getTurn()
        for i in range(1,4):
            f.dropChip(p, i)
        r = f.dropChip(p, 4)
        self.assertEqual(f.check4Horizontal(r[0],r[1]), True)

    def test_fourVertical(self):
        f = FourInLine()
        p = f.getTurn()
        for i in range(3):
            f.dropChip(p, 0)
        r = f.dropChip(p, 0)
        self.assertEqual(f.check4Vertical(r[0],r[1]), True)


if __name__ == '__main__':
    unittest.main()
