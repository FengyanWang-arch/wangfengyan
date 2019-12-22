#coding=utf-8
import unittest
class Test(unittest.TestCase):
    def test01(self):
        a=1
        b=1
        self.assertEqual(a,b,msg='不相等')
    
    def test02(self):
        a="hello"
        b="hello world!"
        self.assertIn(a,b)
        
    def test03(self):
        a=True
        self.assertTrue(a)
        
    def test04(self):
        a="悠悠"
        b="yoyo"
        self.assertEqual(a,b,msg="失败原因：不相等")
        
if __name__=="__main__":
    unittest.main()