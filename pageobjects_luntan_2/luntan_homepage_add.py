# -*- coding: GBK -*-
from pageobjects_luntan_2.base_luntan import basepage
from selenium.webdriver.common.by import By
import time
class Add(basepage):
    admin_center_loc = (By.LINK_TEXT,"管理中心")  # 定位管理中心
    forum_loc=(By.CSS_SELECTOR,"#topmenu li:nth-child(7) a")#定位论坛
    add_new_module_loc=(By.LINK_TEXT,"添加新版块")#定位添加新版块
    submit_button_loc=(By.ID,"submit_editsubmit")#定位确定按钮


    def add(self):
        self.click(*self.admin_center_loc)  # 点击管理中心
        handles=self.driver.window_handles
        self.driver.switch_to.window(handles[1])
        time.sleep(10)
        self.click(*self.forum_loc)#点击论坛
        self.driver.switch_to.frame(0)
        self.click(*self.add_new_module_loc)#点击添加新的板块
        self.click(*self.submit_button_loc)#点击提交按钮
        self.driver.close()
        self.driver.switch_to.window(handles[0])

