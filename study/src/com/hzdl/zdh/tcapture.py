#coding=utf-8
from selenium import webdriver
import time,unittest
from selenium.webdriver.support import expected_conditions as EC
class Login(unittest.TestCase):
    def setUp(self):
        url_login="http://127.0.0.1:81/t18bbs/forum.php"
        self.driver=webdriver.Firefox()
        self.driver.get(url_login)
        
    def test01(self):
        try:
            self.driver.find_element_by_id("ls_username").send_keys("wfy")
            self.driver.find_element_by_id("ls_password").send_keys("111111")
            self.driver.find_element_by_xpath(".//*[@id='lsform']/div/div/table/tbody/tr[2]/td[3]/button").click()
            time.sleep(3)
            tx=self.driver.find_element_by_xpath(".//*[@id='um']/p[1]/strong/a")
#            locator=("xpath",".//*[@id='um']/p[1]/strong/a")
            result=EC.text_to_be_present_in_element(tx,"wl")(self.driver)
            self.assertTrue(result)
        except Exception as msg:
            print("异常原因：%s"%msg)
            nowTime=time.strftime("%Y%m%d.%H%M%S")
            self.driver.get_screenshot_as_file("%s.jpg"%nowTime)
        
    def tearDown(self):
        self.driver.quit()
    
if __name__=="__main__":
    unittest.main()