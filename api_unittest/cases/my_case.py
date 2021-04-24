import unittest
from lib.wanba_request import *
from ddt import ddt,data
from lib.read_case import read_cases


@ddt
class HOME_modular(unittest.TestCase):
	def setUp(self):
		pass
	
	def tearDown(self):
		pass
	
	case_list=read_cases(0)
	
	@data(*case_list)
	def test_home_case(self,data):
		data_re={}
		data_re['url']=data['接口地址']
		data_re['params']=data['请求参数']
		r=post_request(data['请求地址'],data_re)
		r_code=r.status_code
		res=r.json()
		print(res)
		if r_code==200:
			if data['校验参数']=="等于":
				self.assertEqual(res[data['校验字段']],data['预期结果'])
			elif data['校验参数']=="不等于":
				self.assertNotEqual(res[data['校验字段']],data['预期结果'])
			else:
				print('请修改用例')


@ddt
class IM_modular(unittest.TestCase):
	def setUp(self):
		pass
	
	def tearDown(self):
		pass
	
	case_list=read_cases(1)
	
	@data(*case_list)
	def test_im_case(self,data):
		data_re={}
		data_re['url']=data['接口地址']
		data_re['params']=data['请求参数']
		r=post_request(data['请求地址'],data_re)
		r_code=r.status_code
		res=r.json()
		if r_code==200:
			if data['校验参数']=="等于":
				self.assertEqual(res[data['校验字段']],data['预期结果'])
			elif data['校验参数']=="不等于":
				self.assertNotEqual(res[data['校验字段']],data['预期结果'])
			else:
				print('请修改用例')


@ddt
class FEED_modular(unittest.TestCase):
	def setUp(self):
		pass
	
	def tearDown(self):
		pass
	
	case_list=read_cases(2)
	
	@data(*case_list)
	def test_feed_case(self,data):
		data_re={}
		data_re['url']=data['接口地址']
		data_re['params']=data['请求参数']
		r=post_request(data['请求地址'],data_re)
		r_code=r.status_code
		res=r.json()
		if r_code==200:
			if data['校验参数']=="等于":
				self.assertEqual(res[data['校验字段']],data['预期结果'])
			elif data['校验参数']=="不等于":
				self.assertNotEqual(res[data['校验字段']],data['预期结果'])
			else:
				print('请修改用例')


@ddt
class ME_modular(unittest.TestCase):
	def setUp(self):
		pass
	
	def tearDown(self):
		pass
	
	case_list=read_cases(3)
	
	@data(*case_list)
	def test_me_case(self,data):
		data_re={}
		data_re['url']=data['接口地址']
		data_re['params']=data['请求参数']
		r=post_request(data['请求地址'],data_re)
		r_code=r.status_code
		res=r.json()
		if r_code==200:
			if data['校验参数']=="等于":
				self.assertEqual(res[data['校验字段']],data['预期结果'])
			elif data['校验参数']=="不等于":
				self.assertNotEqual(res[data['校验字段']],data['预期结果'])
			else:
				print('请修改用例')


@ddt
class MEET_modular(unittest.TestCase):
	def setUp(self):
		pass
	
	def tearDown(self):
		pass
	
	case_list = read_cases(4)
	
	@data(*case_list)
	def test_me_case(self,data):
		data_re = {}
		data_re['url'] = data['接口地址']
		data_re['params'] = data['请求参数']
		r = post_request(data['请求地址'],data_re)
		r_code = r.status_code
		res = r.json()
		if r_code == 200:
			if data['校验参数'] == "等于":
				self.assertEqual(res[data['校验字段']],data['预期结果'])
			elif data['校验参数'] == "不等于":
				self.assertNotEqual(res[data['校验字段']],data['预期结果'])
			else:
				print('请修改用例')
if __name__=='__main__':
	unittest.main()
