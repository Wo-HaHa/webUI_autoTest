import unittest
import HTMLTestRunner
import os
current_path=os.path.dirname(os.path.realpath(__file__))
reporter_path=os.path.join(current_path,"report")
if not os.path.exists(reporter_path):os.mkdir(reporter_path)
test_dir='./'
suite=unittest.TestLoader().discover(test_dir,pattern="*test.py")
if __name__=="__main__":
    html_report=reporter_path+r"\result.html"
    fp=open(html_report,"wb")
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,verbosity=2,title="单元测试报告",description="用例执行情况")
    runner.run(suite)



