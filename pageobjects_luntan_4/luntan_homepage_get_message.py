# -*- coding: GBK -*-
from pageobjects_luntan_4.base_luntan import basepage
from selenium.webdriver.common.by import By
class Get_Message(basepage):
    title_loc=(By.ID,"thread_subject")#定位投票题目
    first_title_loc=(By.CSS_SELECTOR,".pcht tr:first-of-type label")#定位第一个选项内容
    second_title_loc = (By.CSS_SELECTOR, ".pcht tr:nth-child(3) label")  # 定位第一个选项内容
    third_title_loc = (By.CSS_SELECTOR, ".pcht tr:nth-child(5) label")  # 定位第一个选项内容
    first_percent_loc = (By.CSS_SELECTOR, ".pcht tr:nth-child(2) td:nth-child(2)")  # 定位第一个比例
    second_percent_loc = (By.CSS_SELECTOR, ".pcht tr:nth-child(4) td:nth-child(2)")  # 定位第二个比例
    third_percent_loc = (By.CSS_SELECTOR, ".pcht tr:nth-child(6) td:nth-child(2)")  # 定位第三个比例


    # sumbit_button_loc=(By.NAME,"pollsubmit")#定位到提交按钮

    def get_message(self):
        print("本次投票的标题为：")
        self.get_text(*self.title_loc)  # 获取投票标题
        print(self.get_text(*self.first_title_loc))#获取第一个投票选项的题目
        print("投票比例为：")
        self.get_text(*self.first_percent_loc)# 获取第一个投票的比例
        print(self.get_text(*self.second_title_loc))#获取第二个投票选项的题目
        print("投票比例为：")
        self.get_text(*self.second_percent_loc) # 获取第二个投票的比例
        print(self.get_text(*self.third_title_loc))  # 获取第三个投票选项的题目
        print("投票比例为：")
        self.get_text(*self.third_percent_loc) # 获取第三个投票的比例



