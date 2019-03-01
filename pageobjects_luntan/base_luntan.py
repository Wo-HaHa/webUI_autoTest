from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from framework.logger import Logger
import os
import time

logger=Logger("basepage").getlog()

class basepage(object):
    def __init__(self,driver):
        self.driver=driver
    def get_window_img(self):
        file_path=os.path.dirname(os.path.abspath('.'))+'/screenshots/'
        rq=time.strftime("%Y%m%d%H%M",time.localtime(time.time()))
        screen_name=file_path+rq+'.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            # logger.info("had take and save to folder : /screenshots")
        except Exception as e:
            self.get_window_img()
            logger.error("faild take screenshots!! %s"%e)


    def open_url(self,url):
        self.driver.get(url)
        logger.info("open the browser")
    def quit(self):
        self.driver.quit()
        logger.info("exit current behavior")
    def close(self):
        try:
            self.driver.close()
            logger.info("Closing and quit current browser.")
        except Exception as e:
            self.get_window_img()
            logger.error("Failed to quit the browser with %s"%e)

    def find_element(self,*loc):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))

            return self.driver.find_element(*loc)
            logger.info("找到页面元素%s"%(self.loc))
        except:
            self.get_window_img()
            logger.error("%s页中未找到%s元素" %(self,loc))
    def click(self,*loc):
        el=self.find_element(*loc)
        try:
            el.click()
            logger.info("the element %s was clicked" %el.text)
        except Exception as e:
            self.get_window_img()
            # logger.error("failed to clicked element with %s"%e)
    def clear(self,*loc):
        el=self.find_element(*loc)
        try:
            el.clear()
            logger.info("clear text  in box before typing ")
        except Exception as e:
            self.get_window_img()
            logger.error("faild clear box with %s" %e)


        # self.driver.clear()
    def sendkeys(self,text,*loc):
        el=self.find_element(*loc)
        el.clear()
        try:
            el.send_keys(text)
            logger.info("输入内容%s",text)
        except Exception as e:
            self.get_window_img()
            logger.error("Faild to type in input box with %s" %e)
    def get_text(self,*loc):
        el=self.find_element(*loc)
        try:
            print(el.text)
        except Exception as e:
            logger.error("failed get text")
