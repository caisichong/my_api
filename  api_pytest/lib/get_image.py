# -*- coding: utf-8 -*-
# @Time    : 2021/2/24 12:54 下午
# @Author  : 蔡思冲
# @File    : get_image.py
# @Software: PyCharm
from lib.get_report import get_newreport
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from config.settings import JPG_path
import time


def get_png():
	options=webdriver.ChromeOptions()
	#options.add_argument('--headless')
	options.add_argument('--headless')
	options.add_argument('--dns-prefetch-disable')
	options.add_argument('--no-referrers')
	options.add_argument('--disable-gpu')
	options.add_argument('--disable-audio')
	options.add_argument('--ignore-certificate-errors')
	options.add_argument('--allow-insecure-localhost')
	options.add_argument('window-size=500x900')
	try:
		driver=webdriver.Chrome(options=options)
		driver.maximize_window()
		file_names="file:///%s"%(get_newreport())
		driver.get(file_names)
		jpg_name="%s/%s.png"%(JPG_path,time.strftime("%Y-%m-%d %H%M%S",time.localtime(time.time())))
		time.sleep(3)
		driver.get_screenshot_as_file(jpg_name)
		driver.quit()
	except WebDriverException:
		print("截图失败")
