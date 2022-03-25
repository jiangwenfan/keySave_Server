from django.shortcuts import render,HttpResponse
from functionMoudle.modifyPasswd import modifyPasswd

def modifyApiHandle(request):
	if request.method == 'GET':
		return HttpResponse("request method error")
	else:
		#修改密码
		tableid = request.POST.get('tableId')
		data = {}
		data['siteId'] = request.POST.get('siteId')
		data['sitePasswdEncry'] = request.POST.get('sitePasswdEncry')
		data['siteName'] = request.POST.get('siteName')
		data['siteDomain'] = request.POST.get('siteDomain')
		data['siteLoginUrl'] = request.POST.get('siteLoginUrl')
		data['siteLoginArea'] = request.POST.get('siteLoginArea')
		data['algor'] = request.POST.get('algor')
		print(tableid)

		if modifyPasswd(tableid,data):
			return HttpResponse("修改成功!")
		else:
			return HttpResponse("修改失败!")
