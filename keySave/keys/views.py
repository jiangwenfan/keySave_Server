from django.shortcuts import render,HttpResponse
from keys.handleFunction.addHandle import  addHandle
from keys.handleFunction.selectHandle import selectHandle
from keys.handleFunction.modifyHandle import modifyHandle
from keys.handleFunction.deleteHandle import deleteHandle
from keys.handleFunction.userIndexHandle import userIndexHandle
# Create your views here.

# FileResponse

"""
添加新的密码信息
"""
def addPasswd(request):
	return addHandle(request)

"""
修改密码西信息
"""
def modifyPasswd(request):
    return modifyHandle(request)


"""
删除密码信息
"""
def deletePasswd(request):
    return deleteHandle(request)


"""
查询用户的所有密码信息
"""
def selectPasswd(request):
	return selectHandle(request)


"""
显示登陆后的个人主页显示页面。
"""
def userIndex(request):
    return userIndexHandle(request)
"""

处理登录操作
"""
def login(request):
    pass

"""
处理注册操作
"""
def register(request):
    pass

def index(request):
	return render(request,'index.html')

