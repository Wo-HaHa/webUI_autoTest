from pageobjects_luntan_2.base_luntan import basepage
from selenium.webdriver.common.by import By
class Reply(basepage):
    home_page_post_reply_loc = (By.ID, "post_reply")  # 定位回帖
    home_page_post_reply_content = (By.ID, "postmessage")  # 定位回帖框
    home_page_post_reply_button_loc = (By.ID, "postsubmit")  # 定位回帖按钮
    def reply(self,post_content):
        self.click(*self.home_page_post_reply_loc)  # 点击回帖按钮
        self.sendkeys(post_content, *self.home_page_post_reply_content)  # 发送回帖内容
        self.click(*self.home_page_post_reply_button_loc)  # 点击回帖/参与按钮