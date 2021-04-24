# __author__ = 'ak'


import requests
import json
import sys

def run(msg,urls,atMobiles):
	data1 = {
		"msgtype":"text",
		"text":{
			"content":"事业部今日Bug统计:"+'\n'+msg
			},
		"at":{
			"atMobiles":atMobiles,
			"isAtAll":False
			}
		}
	
	
	header = {'Content-Type':'application/json; charset=utf-8'}
	print(data1)
	temp1 = requests.post(url = urls,data = json.dumps(data1),headers = header)
		
	print(temp1.text)

#
# if __name__ == '__main__':
# 	urls1 = 'https://oapi.dingtalk.com/robot/send?access_token'\
# 	    '=8cf0b365b2929e300f3ced7c622c1f9f08df8d9424b704ffe7cb93a61d11541d'
# 	msg1 = sys.argv[1]
# 	atMobiles1 = []
# 	run(msg = msg1,urls = urls1,atMobiles = atMobiles1)
