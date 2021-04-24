import shutil,time
from config.settings import *
import pytest
from lib.get_report import updateResult,gettouse
from cases.test_case import results

def del_files(file_path):
	ls = os.listdir(file_path)
	for i in ls:
		f_path = os.path.join(file_path,i)
		if os.path.isfile(f_path):
			os.remove(f_path)
		elif os.path.isdir(f_path):
			shutil.rmtree(f_path)

if __name__ == '__main__':
	del_files(TEMP_PATH)
	pytest.main(["--alluredir",TEMP_PATH])  ## 生成测试数据
	allure_cmd = "allure generate ./temp/ -o ./allure-report/ --clean"  ## 将报告转换成html文件格式的命令
	# report = os.popen(allure_cmd,mode = "r")  ## 运行命令，生成测试报告
	report = os.system(allure_cmd)  ## 运行命令，生成测试报告
	time.sleep(2)
	updateResult(results,'客户端','caisichong@moqipobing.com',gettouse()[0],gettouse()[1],gettouse()[2],gettouse()[3])