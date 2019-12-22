#coding=utf-8
import unittest

class Test(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def testMinus(self):
        result=6-5
        hope=1
        self.assertEqual(result,hope)
        
    def testDivide(self):
        result=7/2
        hope=3.5
        self.assertEqual(result,hope)
        
if __name__=='__main__':
    unittest.main()