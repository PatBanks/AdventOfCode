from Day4.Day4P1 import *



class testValid(unittest.TestCase):

    def test_valid_pid(self):
        self.assertTrue(valid_pid('111111111'))
        self.assertFalse(valid_pid('111ad'))

    def test_valid_ecl(self):
        self.assertEqual(valid_ecl('brn'), True)
        self.assertEqual(valid_ecl('der'), False)

    def test_valid_hcl(self):
        self.assertEqual(valid_hcl('#aab123'), True)
        self.assertEqual(valid_hcl('aaaaaaa'), False)

    def test_valid_hgt(self):
        self.assertTrue(valid_hgt('60in'))
        self.assertTrue(valid_hgt('190cm'))
        self.assertFalse(valid_hgt('6in'))
        self.assertFalse(valid_hgt('in'))
        self.assertFalse(valid_hgt('2cin'))

    def test_valid_number(self):
        self.assertEqual(valid_number(2015, 2010, 2020), True)
        self.assertEqual(valid_number(2010, 2010, 2020), True)
        self.assertEqual(valid_number(2009, 2010, 2020), False)


if __name__ == '__main__':
    unittest.main()