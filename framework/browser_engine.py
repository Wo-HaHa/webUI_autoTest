import os.path
from configparser import ConfigParser
from selenium import webdriver
from framework.logger import Logger
logger=Logger("BrowserEngine").getlog()
class BrowserEngine(object):
    dir=os.path.dirname(os.path.abspath("."))
    chrome_path=dir+"/tools/chromedriver.exe"
    Ie_path=dir+"/tools/IEDriver.exe"
    firefox_driver_path = dir + "/tools/geckodriver.exe"

    def open_browser(self):
        config = ConfigParser()
        file_path = os.path.dirname(os.path.abspath(".")) + "/config/config.ini"
        # print(file_path)
        config.read(file_path)

        browser = config.get("browserType", "browserName")
        logger.info("You had select %s browser." % browser)
        url = config.get("testServer", "URL")
        logger.info("The test server url is: %s" % url)

        if browser == "Firefox":
            self.driver = webdriver.Firefox(self.firefox_driver_path)
            logger.info("starting firefox browser.")
        elif browser == "Chrome":
            self.driver = webdriver.Chrome(self.chrome_path)
            logger.info("starting chrome browser.")
        elif browser == "IE":
            self.driver = webdriver.Ie(self.Ie_path)
            logger.info("starting ie browser")

        self.driver.get(url)
        logger.info("open url:%s" % url)
        self.driver.maximize_window()
        logger.info("Maximize the current window")
        self.driver.implicitly_wait(10)
        logger.info("set implicitly wait 10 seconds")
        return self.driver

    def quit_browser(self):
        logger.info("now,close and quit the browser")
        self.driver.quit()

# b=BrowserEngine()
# b.open_browser()