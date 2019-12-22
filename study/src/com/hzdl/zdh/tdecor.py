#coding=utf-8
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import unittest
from time import sleep
class BolgHome(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox()
        url="https://www.cnblogs.com/yoyoketang/"
        cls.driver.get(url)
        sleep(5)
        
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        
    def test01(self):
        locator=("id","blog_nav_sitehome")
        text="博客园"
        result=EC.text_to_be_present_in_element(locator,text)(self.driver)
        self.assertTrue(result)
        
    def test02(self):
        locator=("id","blog_nav_myhome")
        text="首页"
        result=EC.text_to_be_present_in_element(locator,text)(self.driver)
        self.assertTrue(result)
        
if __name__=="__main__":
    unittest.main()
        
        