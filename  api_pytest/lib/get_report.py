from config.settings import REPORT_Path,HTML_path,JPG_path,ALLUREs_PATH
import os,json
import requests

productname='客户端'
def get_newreport():
	all_report = os.listdir(HTML_path)
	all_report.sort(key = lambda fn:os.path.getmtime(HTML_path + "/" + fn))  # 按时间排序
	abs_path = os.path.join(HTML_path,all_report[-1])
	return abs_path


def get_new_report_name():
	all_report = os.listdir(HTML_path)
	all_report.sort(key = lambda fn:os.path.getmtime(HTML_path + "/" + fn))  # 按时间排序
	file_name = all_report[-1]
	return file_name


def get_newpng():
	all_png = os.listdir(JPG_path)
	all_png.sort(key = lambda fn:os.path.getmtime(JPG_path + "/" + fn))  # 按时间排序
	png_path = os.path.join(JPG_path,all_png[-1])
	return png_path


def get_new_png_name():
	all_png = os.listdir(JPG_path)
	all_png.sort(key = lambda fn:os.path.getmtime(JPG_path + "/" + fn))  # 按时间排序
	pog_name = all_png[-1]
	return pog_name


def get_html():
	files = get_newreport()
	with open(files,'r',encoding = "utf-8") as f:
		content_html = f.read()
	return content_html


def insertCaseResponse(resultId,productName,createUserEmail,caseName,url,responseData,actionResult,params):
	data = {}
	data['resultId'] = resultId
	data['productName'] = productName
	data['createUserEmail'] = createUserEmail
	data['caseName'] = caseName
	data['url'] = url
	data['responseData'] = responseData
	data['actionResult'] = actionResult
	data['params'] = params
	datas = json.dumps(data,ensure_ascii = False,skipkeys = True)
	url = 'http://101.200.239.26:5050/apiTest/insertCaseResponse'
	headers = {'Content-Type':'application/json'}
	res = requests.post(url = url,data = datas.encode('utf-8'),headers=headers)
	if res.status_code == 200:
		return res
	else:
		print('错误码为：%s' % (res.status_code))
		print(res.text)


def insertResult():
	res = requests.post(url = 'http://101.200.239.26:5050/apiTest/insertResult')
	if res.status_code == 200:
		return res.json()['data']['resultId']
	else:
		print('错误码为：%s' % (res.status_code))


def judge(res,metadata,resultId):
	r_code = res.status_code
	r = res.json()
	if r_code == 200:
		if metadata['校验参数'] == "等于":
			if r[metadata['校验字段']] == metadata['预期结果']:
				insertCaseResponse(resultId,'客户端','caisichong@moqipobing.com',metadata['用例描述'],metadata['接口地址'],r,
				                   'pass',metadata['请求参数'])
			else:
				insertCaseResponse(resultId,'客户端','caisichong@moqipobing.com',metadata['用例描述'],metadata['接口地址'],r,
				                   'fail',metadata['请求参数'])
		elif metadata['校验参数'] == "不等于":
			if r[metadata['校验字段']] == metadata['预期结果']:
				insertCaseResponse(resultId,'客户端','caisichong@moqipobing.com',metadata['用例描述'],metadata['接口地址'],r,
				                   'pass',metadata['请求参数'])
			else:
				insertCaseResponse(resultId,'客户端','caisichong@moqipobing.com',metadata['用例描述'],metadata['接口地址'],r,
				                   'fail',metadata['请求参数'])
	else:
		print('请求失败了，请检查代码，错误码为：%s' % (r_code))
		insertCaseResponse(resultId,'客户端','caisichong@moqipobing.com',metadata['用例描述'],metadata['接口地址'],r,
		                   'error',metadata['请求参数'])


def updateResult(resultId,productName,createUserEmail,total,passCount,failCount,errorCount):
	data = {}
	data['resultId'] = resultId
	data['productName'] = productName
	data['createUserEmail'] = createUserEmail
	data['total'] = total
	data['passCount'] = passCount
	data['failCount'] = failCount
	data['errorCount'] = errorCount
	print(data)
	url = 'http://101.200.239.26:5050/apiTest/updateResult'
	headers = {'Content-Type':'application/json'}
	res = requests.post(url,data,headers)
	if res.status_code == 200:
		return res
	else:
		print('错误码为：%s' % (res.status_code))


def gettouse():
	filename = ALLUREs_PATH + '/widgets/summary.json'
	print(filename)
	with open(filename) as f:
		toualt = json.load(f)
		pass_case = toualt['statistic']['passed']
		fail_case = toualt['statistic']['failed']
		total_case = toualt['statistic']['total']
		broken_case = toualt['statistic']['broken']
		skipped_case = toualt['statistic']['skipped']
		unknown_case = toualt['statistic']['unknown']
		error_case = broken_case + skipped_case + unknown_case
		print(total_case,pass_case,fail_case,error_case)
		return total_case,pass_case,fail_case,error_case
