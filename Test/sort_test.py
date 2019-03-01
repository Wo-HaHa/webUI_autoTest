from Test.sort import sort
from ddt import  ddt,unpack,data
import unittest
@ddt
class sortTestCase(unittest.TestCase):
    @classmethod
    def setUp(cls):
        print("开始测试----------------")
    @data([0,0,0],[1,0,2],[1,1,10],[1,2,20])
    @unpack
    def test_sort(self,n,m,except_value):
        result=sort(n,m)
        self.assertEqual(result,except_value,msg=result)
    @classmethod
    def tearDown(cls):
        print("结束测试----------------")
if __name__=="__main__":
    unittest.main(verbosity=2)


