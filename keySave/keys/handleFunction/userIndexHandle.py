from django.shortcuts import render
from functionMoudle.getPasswd import getPasswd2

def userIndexHandle(request):
	if request.method == "GET":
		return render(request,"keys/index.html",{'data':getPasswd2("jwf")})
	else:
		pass
