#coding:utf-8
import unittest,time
from common.logger.loggingpack import Log
from selenium import webdriver
log=Log()

class Test(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.get("https://www.baidu.com")
        self.driver.implicitly_wait(30)
        
    def test_01(self):
        log.info("---测试用例开始---")
        self.driver.find_element_by_id('kw').send_keys("python")
        log.info("input content:python")
        self.driver.find_element_by_id('su').click()
        log.info("click button:id=su")
        time.sleep(2)
        t=self.driver.title
        log.info(r"get driver title:%s"%t)
        self.assertIn("百度搜索",t)
        
if __name__=="__main__":
    unittest.main()