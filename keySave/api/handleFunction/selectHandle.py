"""
1.判断请求方式，get时，根据请求id返回json数据
2.获取get请求过来的参数。
3.把参数交给getPasswd函数，获取数据，转为json,返回给前端。
"""
from django.shortcuts import render,HttpResponse
from functionMoudle.getPasswd import getPasswd
import json

def selectApiHandle(request):
	if request.method == "POST":
		siteName = request.POST.get("siteName")
		print(siteName)
		dataList = getPasswd(siteName) #data列表
		datajson = json.dumps(dataList)
		print(datajson)
		return HttpResponse(datajson)
	else:
		return HttpResponse("request method error!")
