from django.shortcuts import render,HttpResponse
from functionMoudle.getOnePasswd import getOnePasswd
from functionMoudle.modifyPasswd import modifyPasswd

def modifyHandle(request):
	if request.method == 'GET':
		return render(request, 'keys/modify.html')
	else:
		tableid = request.POST.get('tableId') #None
		if tableid == None: 
			tableid = request.POST.get('res') #None
			#修改密码
			data = {}
			data['siteId'] = request.POST.get('siteId')
			data['sitePasswdEncry'] = request.POST.get('sitePasswdEncry')
			data['siteName'] = request.POST.get('siteName')
			data['siteDomain'] = request.POST.get('siteDomain')
			data['siteLoginUrl'] = request.POST.get('siteLoginUrl')
			data['siteLoginArea'] = request.POST.get('siteLoginArea')
			data['algor'] = request.POST.get('algor')
			print(data)
			print("--",tableid)
			
			if modifyPasswd(tableid,data):
				return HttpResponse("修改成功!")
			else:
				return HttpResponse("修改失败!")
		else:
			#否则:返回显示的数据.#查询数据，显示到页面上。
			print("else:",tableid)
			info = getOnePasswd(tableid)  #只有一条数据
			return render(request, 'keys/modifyRes.html', {"item":info})
