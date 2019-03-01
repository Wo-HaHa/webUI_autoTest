import unittest
from testsuites.base_testcase import BaseTestCase
from pageobjects.baidu_homepage import HomePage
class BaiDuSearch(BaseTestCase):
    def test_baidu_search(self):
        homepage=HomePage(self.driver)
        # homepage.open_url("https://www.baidu.com")
        homepage.search("java")
if __name__=="__main__":
    unittest.main()

