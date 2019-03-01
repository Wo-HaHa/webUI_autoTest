from pageobjects.base import basepage
from selenium.webdriver.common.by import By
class HomePage(basepage):
    home_page_input_search_loc=(By.CLASS_NAME,"s_ipt")
    home_page_button_search_loc = (By.ID, "su")
    def search(self,content):
        self.sendkeys(content,*self.home_page_input_search_loc)
        self.click(*self.home_page_button_search_loc)