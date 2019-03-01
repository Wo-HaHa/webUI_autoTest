# -*- coding: GBK -*-
from selenium.webdriver.common.by import By
import unittest
from luntan_testsuites.base_luntan_testcase import BaseTestCase
from pageobjects_luntan_2.luntan_homepage_login import Login
from pageobjects_luntan_2.luntan_homepage_public import Public
from pageobjects_luntan_2.luntan_homepage_reply import Reply
from pageobjects_luntan_2.luntan_exit import Exit
from pageobjects_luntan_2.new_model_public import New_Public
from pageobjects_luntan_2.luntan_homepage_add import Add
from pageobjects_luntan_2.luntan_homepage_delete import Delete


import time


class Test_2(BaseTestCase):
    def test_luntan_2(self):
        log = Login(self.driver)
        log.login("sunkai", "19960618")
        self.assertEqual(log.find_element(By.LINK_TEXT, "管理中心").text, "管理中心")
        d=Delete(self.driver)
        d.Delete()

        a=Add(self.driver)
        a.add()

        ex = Exit(self.driver)
        ex.exit()
        self.assertEqual(log.find_element(By.ID,"ls_username").text, '')

        log.login("lixiuzhi","19970803")
        self.assertEqual(log.find_element(By.LINK_TEXT, "退出").text, "退出")

        N_P=New_Public(self.driver)
        N_P.public("1234568789","hahahahahahaha")
        self.assertEqual(N_P.find_element(By.LINK_TEXT, "回复").text, "回复")

        re = Reply(self.driver)
        re.reply("good!!!!!!!!!!")
        self.assertNotEqual(re.find_element(By.CLASS_NAME, "t_f").text, "None")
        ex = Exit(self.driver)
        ex.exit()
        self.assertEqual(N_P.find_element(By.ID, "ls_username").text, '')
        time.sleep(10)


if __name__ == "__main__":
    unittest.main()

