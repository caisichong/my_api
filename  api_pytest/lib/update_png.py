from qiniu import Auth,put_file
from lib.get_report import get_new_png_name,get_newpng


def update_qiniu():
	# 需要填写你的 Access Key 和 Secret Key
	access_key=''
	secret_key=''
	# 构建鉴权对象
	q=Auth(access_key,secret_key)
	# 要上传的空间
	bucket_name='excel-case'
	# 上传后保存的文件名
	key=get_new_png_name().replace(" ", "-")
	# 生成上传token
	token=q.upload_token(bucket_name,key)
	
	# 要上传文件的路径
	localfile=get_newpng()
	ret,info=put_file(token,key,localfile)
	image_file='http://qp2d3dv2z.hn-bkt.clouddn.com/'+ret.get('key')
	print(image_file)
	return image_file
