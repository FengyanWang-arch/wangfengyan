#coding=utf-8
from selenium import webdriver
from time import sleep 
class Screen(object):
    def __init__(self,driver):
        self.driver=driver
        
    def __call__(self,f):
        def inner(*args):
            try:
                return f(*args)
            except:
                import time
                nowTime=time.strftime("%Y_%m_%d_%H_%M_%S")
                self.driver.get_screenshot_as_file("%s.jpg"%nowTime)
                raise
        return inner
    
import unittest
class Test(unittest.TestCase):
    driver=webdriver.Firefox()
    sleep(2)
    
    def setUp(self):
        self.driver.get("https://www.baidu.com")
        sleep(2)
        
    @Screen(driver)
    def test01(self):
        self.driver.find_element_by_id("kw11").send_keys("python")
        self.driver.find_element_by_id("su").click()
        
    @Screen(driver)
    def test02(self):
        self.driver.find_element_by_id("kw").send_keys("yoyo")
        self.driver.find_element_by_id("su").click()
        
#    def tearDown(self):
#        self.driver.quit()
#        sleep(3)
        
if __name__=="__main__":
    unittest.main()