# -*- coding: GBK -*-
from pageobjects_luntan_4.base_luntan import basepage
from selenium.webdriver.common.by import By
class Public(basepage):
    home_page_moren_loc = (By.CSS_SELECTOR, ".fl_tb h2 a")  # 默认版块
    home_page_fatie_loc = (By.ID, "newspecial")  # 开始发帖按钮
    vote_loc=(By.LINK_TEXT,"发起投票")#定位发起投票的位置
    text_input_loc=(By.NAME,"subject")#定位到投票题目的位置
    first_tag_vote_loc=(By.CSS_SELECTOR,"#pollm_c_1 p:nth-child(1) input")#定位到第一个选项的位置
    second_tag_vote_loc = (By.CSS_SELECTOR, "#pollm_c_1 p:nth-child(2) input")  # 定位到第二个选项的位置
    third_tag_vote_loc = (By.CSS_SELECTOR, "#pollm_c_1 p:nth-child(3) input")  # 定位到第三个选项的位置
    public_vote_button_loc=(By.CSS_SELECTOR,".pnpost span")#定位到发起投票的位置

    # home_page_title_loc = (By.NAME, "subject")  # 题目
    # home_page_content_loc = (By.TAG_NAME, "body")  # 内容
    # home_page_post_click_loc = (By.CSS_SELECTOR, ".pnpost span")  # 发布帖子按钮

    def public(self, title, first,second,third):
        self.click(*self.home_page_moren_loc)  # 点击默认版块
        self.click(*self.home_page_fatie_loc)  # 点击开始发帖按钮
        self.click(*self.vote_loc)#点击发起投票
        handle = self.driver.current_window_handle
        self.sendkeys(title,*self.text_input_loc)#输入投票的题目
        self.sendkeys(first,*self.first_tag_vote_loc)#输入第一个选项的题目
        self.sendkeys(second, *self.second_tag_vote_loc)  # 输入第二个选项的题目
        self.sendkeys(third, *self.third_tag_vote_loc)  # 输入第三个选项的题目
        self.driver.switch_to.window(handle)  # 回到当前页面的窗口
        self.click(*self.public_vote_button_loc)#点击投票按钮

        # self.sendkeys(title, *self.home_page_title_loc)  # 输入发帖题目
        # self.driver.switch_to.frame(0)  # 定位内容的ifram
        # self.sendkeys(content, *self.home_page_content_loc)  # 输入帖子内容
        # self.driver.switch_to.window(handle)  # 回到当前页面的窗口
        # self.click(*self.home_page_post_click_loc)  # 点击发布帖子的按钮