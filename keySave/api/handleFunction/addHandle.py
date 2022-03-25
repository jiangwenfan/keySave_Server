"""
1.根据请求方式返回不同的数据。
2.请求POST时，获取数据，传给addPasswd函数
3.跟不同不同的添加，返回不同json数据，是否成功
"""
from functionMoudle.savePasswd import savePasswd
from django.shortcuts import render,HttpResponse

def addApiHandle(request):
	if request.method == "POST":
		data = {}
		data['siteId'] = request.POST.get('siteId')
		data['sitePasswdEncry'] = request.POST.get('sitePasswdEncry')
		data['siteName'] = request.POST.get('siteName')
		data['siteDomain'] = request.POST.get('siteDomain')
		data['siteLoginUrl'] = request.POST.get('siteLoginUrl')
		data['siteLoginArea'] = request.POST.get('siteLoginArea')
		data['algor'] = request.POST.get('algor')
		print(data)

		if savePasswd(data):
			return HttpResponse("add ok")
		else:
			return HttpResponse("add error")
	else:
		return HttpResponse("request method error")
