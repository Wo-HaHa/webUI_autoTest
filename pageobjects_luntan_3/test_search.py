# -*- coding: GBK -*-
from pageobjects_luntan_3.base_luntan import basepage
from selenium.webdriver.common.by import By
import unittest
from selenium import webdriver
class Search(basepage):
    search_loc=(By.NAME,"searchsubmit")#定位搜索按钮
    gaoji_loc=(By.LINK_TEXT,"高级")#定位高级
    test_loc=(By.ID,"srchtxt_1")#定位输入框
    selete_loc=(By.NAME,"srchtype")#定位单选框
    find_loc=(By.CSS_SELECTOR,".pnc")#定位查找按钮
    condition_loc=(By.CSS_SELECTOR,".xs3 strong font")#定位condition
    # title_loc=(By.ID,"thread_subject")#获取当前的帖子题目

    def search(self,content):
        self.click(*self.search_loc)#点击搜索按钮
        handles=self.driver.window_handles
        self.driver.switch_to.window(handles[1])
        self.click(*self.gaoji_loc)#点击高级
        self.sendkeys(content,*self.test_loc)#输入搜索内容
        self.click(*self.selete_loc)#点击单选框
        self.click(*self.find_loc)#点击搜索
        self.click(*self.condition_loc)#点击搜索出来的内容
        aaaaa = self.driver.window_handles
        self.driver.switch_to.window(aaaaa[2])
        # self.get_text(*self.title_loc)#输出text
        assert "haotest" in self.driver.title
