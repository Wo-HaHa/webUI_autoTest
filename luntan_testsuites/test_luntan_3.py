# -*- coding: GBK -*-
import unittest
from luntan_testsuites.base_luntan_testcase import BaseTestCase
from pageobjects_luntan_3.luntan_homepage_login import Login
from pageobjects_luntan_3.test_search import Search
from pageobjects_luntan_3.luntan_exit import Exit
import time
from selenium.webdriver.common.by import By


class Test_3(BaseTestCase):
    def test_luntan_3(self):
        log = Login(self.driver)
        log.login("sunkai", "19960618")
        self.assertEqual(log.find_element(By.LINK_TEXT, "管理中心").text, "管理中心")
        time.sleep(2)
        se=Search(self.driver)
        se.search("haotest")
        ex=Exit(self.driver)
        ex.exit()
        self.assertEqual(ex.find_element(By.ID, "ls_username").text, '')
        time.sleep(10)


if __name__ == "__main__":
    unittest.main()