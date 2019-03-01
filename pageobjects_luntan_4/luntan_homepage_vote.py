from pageobjects_luntan_4.base_luntan import basepage
from selenium.webdriver.common.by import By
class Vote(basepage):
    first_selete_loc=(By.ID,"option_1")#定位第一个选项框
    sumbit_button_loc=(By.NAME,"pollsubmit")#定位到提交按钮

    def vote(self):
        self.click(*self.first_selete_loc)#点击第一个选择框
        self.click(*self.sumbit_button_loc)#点击提交按钮

