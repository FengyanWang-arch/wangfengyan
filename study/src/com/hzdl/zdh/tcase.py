#coding=utf-8
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import unittest
profile_directory=r"C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\pwaxlqc6.default"
profile=webdriver.FirefoxProfile(profile_directory)

class Blog(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox(profile)
        self.driver.get("http://www.cnblogs.com/yoyoketang")
        print(self.driver.title)
        
    def test_blog(self):
        sleep(3)
        result=EC.title_is(r'上海-悠悠 - 博客园')(self.driver)
        print(result)
        self.assertTrue(result)
        
    def tearDown(self):
        self.driver.quit()
        
if __name__=="__main__":
    unittest.main()