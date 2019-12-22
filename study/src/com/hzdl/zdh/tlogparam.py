#coding=utf-8
from selenium import webdriver
from time import sleep
import unittest

class Login(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.get("http://127.0.0.1:81/t18bbs/forum.php")
        sleep(2)
        
    def login(self,user,psw):
        self.driver.find_element_by_id("ls_username").send_keys(user)
        self.driver.find_element_by_id("ls_password").send_keys(psw)
        self.driver.find_element_by_xpath(".//*[@id='lsform']/div/div/table/tbody/tr[2]/td[3]/button").click()
        sleep(2)
        
    def test01(self):
        self.login("wfy","111111")
        result=self.driver.find_element_by_xpath(".//*[@id='um']/p[1]/strong/a").text
        self.assertEqual(result,"wfy",msg="判断相等")
        sleep(3)
        
    def test02(self):
        self.login("zly","111111")
        result=self.driver.find_element_by_xpath(".//*[@id='um']/p[1]/strong/a").text
        self.assertEqual(result,"zly")
        sleep(3)
        
    def tearDown(self):
        self.driver.quit()
        sleep(2)
        
if __name__=="__main__":
    unittest.main()
            
        