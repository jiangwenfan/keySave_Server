from django.shortcuts import render,HttpResponse
from functionMoudle.deletePasswd import deletePasswd

def deleteApiHandle(request):
	if request.method == 'GET':
		return HttpResponse("request method error!")
	else:
		tableId = request.POST.get('tableId')
		print(tableId)
		#传入需要删除的id
		status = deletePasswd(tableId)
		return HttpResponse(status)

