from Test.abs import abs
from ddt import ddt,unpack,data
import unittest
@ddt
class AbsTestCase(unittest.TestCase):
    def setUp(self):
        print("开始一个测试")
    @data([-1,1],[1,1],[0,0])
    @unpack
    def test_jj(self,n,except_value):
        result=abs(n)
        self.assertEqual(result,except_value,msg=result)
    def tearDown(self):
        print("结束。。。。。。。。")
if __name__=="__main__":
    unittest.main(verbosity=2)


