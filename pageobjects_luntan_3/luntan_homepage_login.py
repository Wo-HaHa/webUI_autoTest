
from pageobjects_luntan_3.base_luntan import basepage
from selenium.webdriver.common.by import By
class Login(basepage):
    home_page_input_yonghu_search_loc=(By.ID,"ls_username")#定位用户框
    home_page_input_pwd_search_loc = (By.ID, "ls_password")#密码框
    home_page_button_loc=(By.CSS_SELECTOR, "em")#登录按钮

    def login(self,admin,pwd):
        self.sendkeys(admin,*self.home_page_input_yonghu_search_loc)#输入用户
        self.sendkeys(pwd, *self.home_page_input_pwd_search_loc)#输入密码
        self.click(*self.home_page_button_loc)#点击登录





