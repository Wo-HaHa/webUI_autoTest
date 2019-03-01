from pageobjects_luntan_2.base_luntan import basepage
from selenium.webdriver.common.by import By
class Delete(basepage):
    home_page_moren_loc = (By.CSS_SELECTOR, ".fl_tb h2 a")  # 默认版块
    home_page_selete_loc = (By.NAME, "moderate[]")  # 开始发帖按钮
    home_page_delete_loc=(By.CSS_SELECTOR,"#mdly strong:nth-child(1) a")#选中删除
    home_page_confirm_loc=(By.ID,"modsubmit")#定位确定的位置

    # home_page_title_loc = (By.NAME, "subject")  # 题目
    # home_page_content_loc = (By.TAG_NAME, "body")  # 内容
    # home_page_post_click_loc = (By.CSS_SELECTOR, ".pnpost span")  # 发布帖子按钮

    def Delete(self):
        self.click(*self.home_page_moren_loc)  # 点击默认版块
        self.click(*self.home_page_selete_loc)  # 选中删帖的框
        self.click(*self.home_page_delete_loc)#点击删除
        self.click(*self.home_page_confirm_loc)#点击确定按钮

        # handle = self.driver.current_window_handle
        # self.sendkeys(title, *self.home_page_title_loc)  # 输入发帖题目
        # self.driver.switch_to.frame(0)  # 定位内容的ifram
        # self.sendkeys(content, *self.home_page_content_loc)  # 输入帖子内容
        # self.driver.switch_to.window(handle)  # 回到当前页面的窗口
        # self.click(*self.home_page_post_click_loc)  # 点击发布帖子的按钮