# -*- coding: utf-8 -*-
# @Time    : 2021/4/2 11:49 上午
# @Author  : 蔡思冲
# @File    : get_tick.py
# @Software: PyCharm
import json
from lib.wanba_request import *

def get_toicket(uid):
	data={}
	data['url']=''
	data['host']=''
	params={}
	params['uid']=uid
	params['type']='0'
	data['params']=json.dumps(params,ensure_ascii=False)
	r=post_request(msurl,data)
	r_json=r.json()
	tick=r_json['data']['ticket']
	return tick

def judge_key(my_dict):
	if 'uid' in json.loads(my_dict['请求参数']):
		uid = json.loads(my_dict['请求参数'])['uid']
		get_toicket(uid)
	elif '__t_' in json.loads(my_dict['请求参数']):
		uid = json.loads(my_dict['请求参数'])['__t_']
		get_toicket(uid)
	else:
		print('不需要获取t票')