from config.settings import REPORT_Path,HTML_path,JPG_path
import os


def get_newreport():
	all_report=os.listdir(HTML_path)
	all_report.sort(key=lambda fn:os.path.getmtime(HTML_path+"/"+fn))  # 按时间排序
	abs_path=os.path.join(HTML_path,all_report[-1])
	return abs_path


def get_new_report_name():
	all_report=os.listdir(HTML_path)
	all_report.sort(key=lambda fn:os.path.getmtime(HTML_path+"/"+fn))  # 按时间排序
	file_name=all_report[-1]
	return file_name


def get_newpng():
	all_png=os.listdir(JPG_path)
	all_png.sort(key=lambda fn:os.path.getmtime(JPG_path+"/"+fn))  # 按时间排序
	png_path=os.path.join(JPG_path,all_png[-1])
	return png_path


def get_new_png_name():
	all_png=os.listdir(JPG_path)
	all_png.sort(key=lambda fn:os.path.getmtime(JPG_path+"/"+fn))  # 按时间排序
	pog_name=all_png[-1]
	return pog_name


def get_html():
	files=get_newreport()
	with open(files,'r',encoding="utf-8") as f:
		content_html=f.read()
	return content_html
