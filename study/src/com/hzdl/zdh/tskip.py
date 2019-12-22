#coding=utf-8
import unittest
@unittest.expectedFailure
class Test(unittest.TestCase):
#    @unittest.skip("无条件跳过此用例")
    def test_1(self):
        print("测试1")
        
#    @unittest.skipIf(True,"为True的时候跳过")
    def test_2(self):
        print("测试2")
        
#    @unittest.skipUnless(False,"为False的时候跳过")
    def test_3(self):
        print("测试3")
        
#    @unittest.expectedFailure
    def test_4(self):
        print("测试4")
        self.assertEqual(2,2)
        self.assertEqual(6,6)
        self.assertEqual(2,3)
        
if __name__=="__main__":
    unittest.main()