import configparser
from config.settings import CONFIGS_PATH


def configs():  #拿到配置文件中的值，并放到字典中
	cf=configparser.ConfigParser()
	cf.read(CONFIGS_PATH+"/config.ini")
	dicts=[]
	for sections in cf.sections():
		for items in cf.items(sections):
			dicts.append(items)
	return dict(dicts)
