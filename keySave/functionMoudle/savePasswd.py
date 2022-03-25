#from keys.module import desCrypt
from keys.models import Allkeys

"""
1.创建密码表的条目对象
2.根据传入值进行数据库插入
3.根据插入结果返回True或False
"""
def savePasswd(data):
	record = Allkeys()
	record.siteId = data['siteId']
	record.sitePasswdEncry=data['sitePasswdEncry'] 
	record.siteName = data['siteName']
	record.siteDomain = data['siteDomain']
	record.siteLoginUrl = data['siteLoginUrl']
	record.siteLoginArea=data['siteLoginArea'] 
	record.algor = data['algor'] 
	#res = desCrypt.des_encrypt(passwd)
	#record.passwdEncry = str(res, encoding="utf-8")
	# print(res)
	record.key = "KUf4hM5rThssysJhcRFCfxLR8Imihjl0eMsyhh1M7Wk" #deafult
	record.save()
	return True
