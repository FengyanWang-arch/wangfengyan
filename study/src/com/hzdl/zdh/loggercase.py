#coding=utf-8
import unittest
import logging
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from time import sleep

logger=logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler_critical=logging.FileHandler('critical_log.txt','w')
handler_critical.setLevel(logging.WARNING)

handler_info=logging.StreamHandler()
handler_info.setLevel(logging.INFO)

formatter=logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
handler_critical.setFormatter(formatter)
handler_info.setFormatter(formatter)

logger.addHandler(handler_info)
logger.addHandler(handler_critical)

class YoutubeSearch(unittest.TestCase):
    def setUp(self):
        logger.info("打开火狐")
        self.browser=webdriver.Firefox()
        self.browser.get("https://www.baidu.com")
        logger.info("打开百度页面")
        
    def tearDown(self):
        logger.info("截图")
        self.browser.save_screenshot("photo.png")
#        self.browser.quit()
#        logger.info("退出浏览器")
        
    def test_youtube_search(self):
        logger.info("断言title")
        
        try:
            self.assertIn("百度一下，你就知道",self.browser.title)
#            sleep(3)
            searchElement=self.browser.find_element_by_id("kw")
#            sleep(3)
            
        except AssertionError:
            logger.critical("断言失败",exc_info=True)
            self.fail("断言失败1")
            
        except NoSuchElementException:
            logger.critical("没有这个元素",exc_info=True)
            self.fail("没有这个元素2")
            
        else:
            searchElement.send_keys("selenium python")
            sleep(3)
            searchElement.send_keys(Keys.RETURN)
            sleep(3)
            logger.info("查询")
            
if __name__=="__main__":
    unittest.main(exit=False,warnings='ignore')
        
    