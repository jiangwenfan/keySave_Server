from django.shortcuts import render
from functionMoudle.getPasswd import getPasswd

def selectHandle(request):
	if request.method == "GET":
		return render(request,"keys/show.html")
	else:
		siteName = request.POST.get('siteName')
		print(siteName)
		data = getPasswd(siteName) #列表
		return render(request, 'keys/showRes.html', {"data":data})
