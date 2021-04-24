import unittest,time
from lib.send_mail import sendmail
from lib.get_report import get_html,get_newreport,get_newpng
from config.read_config import configs
from BeautifulReport import BeautifulReport
from config.settings import *
from cases.my_case import HOME_modular,IM_modular,FEED_modular,ME_modular,MEET_modular
from lib.get_image import get_png
from lib.send_dingding import send_msg
from lib.update_png import update_qiniu


def send_beautifulreport():
	suite=unittest.TestSuite()  # 建立测试集合
	# test_case=[HOME_CASE,IM_CASE,FEED_CASE,ME_CASE]
	# suite.addTests(unittest.makeSuite(test_case))
	suite.addTest(unittest.makeSuite(HOME_modular))
	suite.addTest(unittest.makeSuite(IM_modular))
	suite.addTest(unittest.makeSuite(FEED_modular))
	suite.addTest(unittest.makeSuite(ME_modular))
	suite.addTest(unittest.makeSuite(MEET_modular))
	filename=time.strftime("%Y-%m-%d %H%M%S",time.localtime(time.time()))+'.html'
	result=BeautifulReport(suite)
	result.report(description='平台基础接口测试报告',filename="request_report.html",report_dir=HTML_path) #发报告
	# get_png() #给报告截图
	# send_msg() #发送钉钉消息


# sendmail(configs(),get_html(),get_newpng()) #发送邮件

send_beautifulreport()
