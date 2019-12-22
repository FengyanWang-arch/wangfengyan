#coding=utf-8
import ddt
import unittest
testdata=[{"username":"wfy名","psw":"111111"},
          {"username":"zly姓","psw":"222222"},
          {"username":"xnn","psw":"333333"}]

@ddt.ddt
class Test(unittest.TestCase):
    def setUp(self):
        print("start!")
        
    def tearDown(self):
        print("end!")
        
    @ddt.data(*testdata)
    def test_ddt(self,data):
        print(data)
        
if __name__=="__main__":
    unittest.main()