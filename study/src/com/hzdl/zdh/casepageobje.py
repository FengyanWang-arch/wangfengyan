#coding=utf-8
import unittest
from secondpack import browser
from basepageobje import login_url,LoginPage

class Login_test(unittest.TestCase):
    def setUp(self):
        self.driver=browser()
        self.login=LoginPage(self.driver)
        self.login.open(login_url)
        
    def login_case(self,username,psw,expect=True):
        self.login.login(username,psw)
        result=self.login.is_text_in_element(("xpath",".//*[@id='um']/p[1]/strong/a"),"wfy")
        self.assertEqual(result,expect)
        
    def test_login01(self):
        self.login_case("wfy","111111")
        
    def test_login02(self):
        self.login_case("wfy","222222")
        
    def tearDown(self):
        self.driver.quit()
        
if __name__=="__main__":
    unittest.main()        