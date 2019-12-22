#coding:utf-8
import unittest
from selenium import webdriver
from ddt import ddt,data,unpack
from time import sleep

@ddt
class developTest(unittest.TestCase):
    def setUp(self):
        profile_directory=r"C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\pwaxlqc6.default"
        profile=webdriver.FirefoxProfile(profile_directory)
        self.driver=webdriver.Firefox(profile)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get('https://www.baidu.com')
#        self.addCleanup(self.driver.quit)
        
    @data(('','','请您输入手机/邮箱/用户名'),('15223387597','','请您输入密码'),('admin','admin','用户名或密码有误，请重新输入或找回密码'))
    @unpack
    def testLogin(self,sendvalue1,sendvalue2,expected):
        self.driver.find_element_by_link_text('登录').click()
        sleep(2)
#        self.driver.find_element_by_id("TANGRAM__PSP_10__footerULoginBtn").click()
#        js='document.getElementById("TANGRAM__PSP_10__footerULoginBtn").click()'
#        self.driver.execute_script(js)
#        self.driver.find_element_by_class_name("tang-pass-footerBar").click()
#        self.driver.find_element_by_id('TANGRAM__PSP_10__footerULoginBtn').click()
   
        sleep(2)
        username=self.driver.find_element_by_id('TANGRAM__PSP_10__userName')
        username.clear()
        username.send_keys(sendvalue1)
        password=self.driver.find_element_by_id('TANGRAM__PSP_10__password')
        password.clear()
        password.send_keys(sendvalue2)
        self.driver.find_element_by_id("TANGRAM__PSP_10__submit").click()
        sleep(3)
        errorText=self.driver.find_element_by_id('TANGRAM__PSP_10__error').text
        self.assertTrue(errorText,expected)
        
    def tearDown(self):
        self.driver.quit()
        
if __name__=='__main__':
        unittest.main(verbosity=2)
        