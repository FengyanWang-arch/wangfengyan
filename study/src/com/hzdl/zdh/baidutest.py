#coding:utf-8
from selenium import webdriver
#from zope.location import Location
from ddt import ddt,data,unpack
import unittest
import cvsfile

@ddt
class BaiduTest(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get("https://www.baidu.com")
        
    @data(*cvsfile.getCsv("d:\\test.csv"))  #产生测试值
    @unpack   #分解测试值
    def testCase_01(self,actual,expect):
        self.driver.find_element_by_id('kw').send_keys(actual)
        import time
        time.sleep(3)
        
    def tearDown(self):
        self.driver.quit()
        
if __name__=="__main__":
#    unittest.main()
    suite=unittest.TestLoader().loadTestsFromTestCase(BaiduTest)
    unittest.TextTestRunner(verbosity=2).run(suite)