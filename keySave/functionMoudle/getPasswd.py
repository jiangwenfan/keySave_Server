#from keys.module import desCrypt
from keys.models import Allkeys

def getPasswd(siteName):
	allData = Allkeys.objects.filter(siteName__contains=siteName)
	print(allData)
	resData = []
	for data in allData:
		print(data)
		item = {}  # 單個項目
		item['id']=data.id
		item['siteId'] = data.siteId
		#item['passwd'] = str(desCrypt.des_descrypt(data.passwdEncry), encoding="utf-8")
		item['sitePasswdEncry'] = data.sitePasswdEncry
		item['siteName'] = data.siteName
		item['siteDomain'] = data.siteDomain
		item['siteLoginUrl'] = data.siteLoginUrl
		item['siteLoginArea'] = data.siteLoginArea
		item['key'] = data.key
		item['algor'] = data.algor
		resData.append(item)
	print(resData)
	return resData

def getPasswd2(userName):
	allData = Allkeys.objects.filter(userName=userName)
	print(allData)
	resData = []
	for data in allData:
		print(data)
		item = {}  # 單個項目
		item['userName']=data.userName
		item['id']=data.id
		item['siteId'] = data.siteId
		#item['passwd'] = str(desCrypt.des_descrypt(data.passwdEncry), encoding="utf-8")
		item['sitePasswdEncry'] = data.sitePasswdEncry
		item['siteName'] = data.siteName
		item['siteDomain'] = data.siteDomain
		item['siteLoginUrl'] = data.siteLoginUrl
		item['siteLoginArea'] = data.siteLoginArea
		item['key'] = data.key
		item['algor'] = data.algor
		resData.append(item)
	print(resData)
	return resData
