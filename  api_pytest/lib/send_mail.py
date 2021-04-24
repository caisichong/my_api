import zmail


def sendmail(config_vale,conntent_html,mail_file):  #用zmail发送邮件
	# 你的邮件内容
	mail_content={
		"subject":config_vale['subject'],  # 邮件主题
		"Content_html":conntent_html,  # 邮件内容
		"Attachments":mail_file  # 邮件附件
		}
	# 使用你的邮件账户名和密码登录服务器
	server=zmail.server(
		username=config_vale['user'],  #邮件用户名
		password=config_vale['password'],  #邮件密码
		smtp_host=config_vale['host'],  #邮件host
		smtp_port=int(config_vale['port']),  #邮件端口
		smtp_ssl=True  #ssl设置
		)
	# 发送邮件
	server.send_mail([config_vale['to_mail']],mail_content)  #发送给多个人
