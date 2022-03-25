# Create your views here.
from api.handleFunction.selectHandle import selectApiHandle
from api.handleFunction.addHandle import addApiHandle
from api.handleFunction.modifyHandle import modifyApiHandle
from api.handleFunction.deleteHandle import deleteApiHandle

def addPasswd(request):
    return addApiHandle(request)

def selectPasswd(request):
	return selectApiHandle(request)

def modifyPasswd(request):
	return modifyApiHandle(request)

def deletePasswd(request):
	return deleteApiHandle(request)
