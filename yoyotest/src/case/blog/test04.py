#coding=utf-8
from selenium import webdriver
import unittest
from time import sleep


class Bolg(unittest.TestCase):
    def setUp(self):
        profile_directory=r"C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\pwaxlqc6.default"
        profile=webdriver.FirefoxProfile(profile_directory)
        self.driver=webdriver.Firefox(profile)
        url="http://127.0.0.1:81/t18bbs/forum.php"
        self.driver.get(url)
        sleep(5)
        
    def login(self,username,psw):
        self.driver.find_element_by_id("ls_username").send_keys(username)
        self.driver.find_element_by_id("ls_password").send_keys(psw)
        self.driver.find_element_by_xpath(".//*[@id='lsform']/div/div/table/tbody/tr[2]/td[3]/button").click()
        sleep(3)
    
    def is_login_sucess(self):
        try:
            text=self.driver.find_element_by_xpath(".//*[@id='um']/p[1]/strong/a").text
            print(text)
            return True
        except:
            return False
    def test_01(self):
        '''测试登录测试用例，账号：wfy,密码：111111 '''
        self.login("wfy","111111")
        result=self.is_login_sucess()
        self.assertTrue(result)
        sleep(3)
        
    def test_02(self):
        self.login("wfy","111111")
        result=self.is_login_sucess()
        self.assertTrue(result)
        sleep(3)
        
    def tearDown(self):
        self.driver.quit()
        sleep(3)
        
if __name__=="__main__":
    unittest.main()