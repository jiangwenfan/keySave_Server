from keys.models import Allkeys

def modifyPasswd(tableid,data):
	print(tableid)
	print(data)
	record = Allkeys.objects.get(id=tableid)
	print(record)

	record.siteId = data['siteId']
	record.sitePasswdEncry = data['sitePasswdEncry']
	record.siteName = data['siteName']
	record.siteDomain = data['siteDomain']
	record.siteLoginUrl = data['siteLoginUrl']
	record.siteLoginArea = data['siteLoginArea']
	record.algor = data['algor']
	print(record)

	record.save()
	return True

