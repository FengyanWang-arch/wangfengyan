#coding:utf-8
import unittest
from time import sleep
class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("start!")
        
    @classmethod
    def tearDownClass(cls):
        sleep(1)
        print("end!")
        
    def test01(self):
        print("用例1")
        
    def test03(self):
        print("用例3")
        
    def test02(self):
        print("用例2")
        
    def addtest(self):
        print("add方法")
        
if __name__=="__main__":
    unittest.main()