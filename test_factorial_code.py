#!/usr/bin/env python3

import unittest
from math import factorial

class TestFactorial(unittest.TestCase):
    '''
    Our basic test class

    '''

    def test_fact(self):
        '''
        The Actual test.
        Any method which starts with ``test_`` will considered as a testcase 
        '''
        res = factorial(5)
        self.assertEqual(res, 120)

    def test_error(self):
       '''
       To test exception raise due to run time error

       '''
       self.assertRaises(ZeroDivisionError, division, 0)

if __name__ == '__main__':
    unittest.main()



if __name__ == '__main__':
    unittest.main()
