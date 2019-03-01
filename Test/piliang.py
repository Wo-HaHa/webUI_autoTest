import unittest
from Test.abs_test import AbsTestCase
from Test.sort_test import sortTestCase

#构建测试套件
suit=unittest.TestSuite()
suit.addTest(unittest.makeSuite(AbsTestCase))
suit.addTest(unittest.makeSuite(sortTestCase))
if __name__=="__main__":
    #执行用例
    runner=unittest.TextTestRunner(verbosity=2)
    runner.run(suit)
