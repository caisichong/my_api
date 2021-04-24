import os
import openpyxl
from config.settings import EXCEL_PATH


def read_cases(sheet_int):
	file_name=EXCEL_PATH+'/平台接口测试用例.xlsx'
	work=openpyxl.load_workbook(file_name)
	sheets=work.worksheets[sheet_int]
	row_num=sheets.max_row
	case_list=[]
	one_list=[]
	for cell in sheets[1]:
		one_list.append(cell.value)
	for i in range(2,row_num+1):
		other_list=[]
		for j in sheets[i]:
			other_list.append(j.value)
		compress_list=dict(zip(one_list,other_list))
		case_list.append(compress_list)
	return case_list

