# -*- coding: GBK -*-
import unittest
from luntan_testsuites.base_luntan_testcase import BaseTestCase
from pageobjects_luntan.luntan_homepage_login import Login
from pageobjects_luntan.luntan_homepage_public import Public
from pageobjects_luntan.luntan_homepage_reply import Reply
from selenium.webdriver.common.by import By
from pageobjects_luntan.luntan_exit import Exit
import time
class Test_1(BaseTestCase):
    def test_luntan_1(self):
        log=Login(self.driver)
        log.login("sunkai","19960618")
        self.assertEqual(log.find_element(By.LINK_TEXT,"管理中心").text,"管理中心")
        p=Public(self.driver)
        p.public("title","12345648789")
        self.assertEqual(log.find_element(By.LINK_TEXT,"回复").text,"回复")
        re=Reply(self.driver)
        re.reply("nice!!!!!!!!!!")
        self.assertNotEqual(log.find_element(By.CLASS_NAME,"t_f").text,"None")
        # ex=Exit(self.driver)
        # ex.exit()
        # time.sleep(5)

if __name__=="__main__":
    unittest.main()

