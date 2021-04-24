# -*- coding: utf-8 -*-
# @Time    : 2021/2/24 6:25 下午
# @Author  : 蔡思冲
# @File    : send_dingding.py
# @Software: PyCharm

from lib.update_png import update_qiniu
from lib.updata_html import update_qiniu_html
import requests,json,time


def send_msg():
	url='https://oapi.dingtalk.com/robot/send?access_token'\
	    '=8cf0b365b2929e300f3ced7c622c1f9f08df8d9424b704ffe7cb93a61d11541d'
	headers={'Content-Type':'application/json;charset=utf-8'}
	data={
		"msgtype":"markdown",
		"markdown":{
			"title":"接口测试报告",
			"text":""+
			       "> \n\n"+
			       "> ![screenshot](%s)\n"%(update_qiniu())+
			       "> #####  [点击查看报告详情](%s)     %s\n"%(update_qiniu_html(),time.strftime("%Y-%m-%d %H%M%S",time.localtime(time.time())))
			},
		"at":{
			"isAtAll":False
			}
		}
	r=requests.post(url,data=json.dumps(data),headers=headers)
	return r.text
