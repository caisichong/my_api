import pytest
import allure
import json
from lib.wanba_request import *
from lib.read_case import read_cases
from config.settings import *
from lib.get_report import *
from lib.get_tick import *
results = insertResult()


class Test_home:
	case_list = read_cases(0)
	@allure.title('{home[用例描述]}')
	@allure.feature('首页')
	@pytest.mark.parametrize("home",case_list)
	def test_home_case(self,home):
		judge_key(home)
		data_re = {}
		data_re['url'] = home['接口地址']
		data_re['params'] = home['请求参数']
		r = post_request(home['请求地址'],data_re)
		r_code = r.status_code
		res = r.json()
		judge(r,home,results)
		if r_code == 200:
			if home['校验参数'] == "等于":
				assert res[home['校验字段']] == home['预期结果']
			elif home['校验参数'] == "不等于":
				assert res[home['校验字段']] != home['预期结果']
		
		else:
			pass


class Test_IM:
	case_list2 = read_cases(1)
	@allure.title('{im[用例描述]}')
	@allure.epic('消息')
	@pytest.mark.parametrize("im",case_list2)
	def test_IM_case(self,im):
		judge_key(im)
		data_re = {}
		data_re['url'] = im['接口地址']
		data_re['params'] = im['请求参数']
		r = post_request(im['请求地址'],data_re)
		r_code = r.status_code
		res = r.json()
		judge(r,im,results)
		if r_code == 200:
			if im['校验参数'] == "等于":
				assert res[im['校验字段']] == im['预期结果']
			elif im['校验参数'] == "不等于":
				assert res[im['校验字段']] != im['预期结果']
		else:
			pass


class Test_feed:
	case_list = read_cases(2)
	idss = []
	for i in case_list:
		idss.append(i['用例描述'])
	@allure.title('{feed[用例描述]}')
	@allure.epic('社区')
	@pytest.mark.parametrize("feed",case_list,ids = idss)
	def test_feed_case(self,feed):
		judge_key(feed)
		data_re = {}
		data_re['url'] = feed['接口地址']
		data_re['params'] = feed['请求参数']
		r = post_request(feed['请求地址'],data_re)
		r_code = r.status_code
		res = r.json()
		judge(r,feed,results)
		if r_code == 200:
			if feed['校验参数'] == "等于":
				assert res[feed['校验字段']] == feed['预期结果']
			elif feed['校验参数'] == "不等于":
				assert res[feed['校验字段']] != feed['预期结果']
		else:
			pass


class Test_me:
	case_list2 = read_cases(3)
	
	@allure.title('{me[用例描述]}')
	@allure.epic('我的')
	@pytest.mark.parametrize("me",case_list2)
	def test_me_case(self,me):
		judge_key(me)
		data_re = {}
		data_re['url'] = me['接口地址']
		data_re['params'] = me['请求参数']
		r = post_request(me['请求地址'],data_re)
		r_code = r.status_code
		res = r.json()
		judge(r,me,results)
		if r_code == 200:
			if me['校验参数'] == "等于":
				assert res[me['校验字段']] == me['预期结果']
			elif me['校验参数'] == "不等于":
				assert res[me['校验字段']] != me['预期结果']
		else:
			pass


class Test_meet:
	case_list2 = read_cases(4)
	
	@allure.epic('遇见')
	@allure.title('{meet[用例描述]}')
	@pytest.mark.parametrize("meet",case_list2)
	def test_me_case(self,meet):
		judge_key(meet)
		data_re = {}
		data_re['url'] = meet['接口地址']
		data_re['params'] = meet['请求参数']
		r = post_request(meet['请求地址'],data_re)
		r_code = r.status_code
		res = r.json()
		judge(r,meet,results)
		if r_code == 200:
			if meet['校验参数'] == "等于":
				assert res[meet['校验字段']] == meet['预期结果']
			elif meet['校验参数'] == "不等于":
				assert res[meet['校验字段']] != meet['预期结果']
		else:
			pass
