#coding=utf-8
from selenium import webdriver
import unittest
from login_pub import Login_Blog
from time import sleep

login_url="http://127.0.0.1:81/t18bbs/forum.php"

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.get(login_url)
        
    def tearDown(self):
        self.driver.quit()
        
    def testlogin(self):
        Login_Blog(self.driver).login("wfy","111111")
        sleep(10)
        
if __name__=="__main__":
    unittest.main()
    