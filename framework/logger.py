import logging
import time
import os.path
class Logger(object):
    def __init__(self,log):
        self.logger=logging.getLogger(log)
        self.logger.setLevel(logging.DEBUG)
        rq=time.strftime("%Y%m%d%h%M",time.localtime(time.time()))
        log_path=os.path.dirname(os.path.abspath("."))+'/logs/'
        log_name=log_path+rq+'.log'

        fh=logging.FileHandler(log_name)
        fh.setLevel(logging.INFO)
        #输出到控制台
        ch=logging.StreamHandler()
        ch.setLevel(logging.INFO)
        #给logger添加handle
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)
        #定义handle输出格式
        formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        fh.setFormatter(formatter)
    def getlog(self):
        return self.logger