import os,sys

BASE_PATH=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPORT_Path=os.path.join(BASE_PATH,'report')
API_PATH=os.path.join(BASE_PATH,'APIS')
HTML_path=os.path.join(REPORT_Path,'html')
JPG_path=os.path.join(REPORT_Path,'jpg')
CASE_PATH=os.path.join(BASE_PATH,'cases')
EXCEL_PATH=os.path.join(BASE_PATH,'cases/excel')
CONFIG_PATH=os.path.join(BASE_PATH,'config.ini')
CONFIGS_PATH=os.path.join(BASE_PATH,'config')
sys.path.insert(0,BASE_PATH)
print(CONFIG_PATH)
