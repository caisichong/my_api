import requests

msurl = ''
apiurl = ''
weburl = ''
rpcurl =''
header={'content-type':"application/x-www-form-urlencoded"}


def post_request(url,data,cookie=None):
	headers={'content-type':"application/x-www-form-urlencoded"}
	r=requests.post(url,data,headers=headers,cookies=cookie,timeout=120)
	return r


def my_request(method,url,data,headers):
	try:
		if method.upper()=='GET':
			r=requests.get(url,data,headers=headers).json()
		else:
			r=requests.post(url,data,headers=headers).json()
	except Exception as e:
		return '出错了，错误是%s'%e
	return r
