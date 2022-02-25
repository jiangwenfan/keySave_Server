from django.shortcuts import render
from cryption import desEncryption,desDecryption
# Create your views here.

"""
处理表单函数,添加新的密码信息
"""
def addPassword(request):
    #plaintext = request.
    pwdPlaintext = "admin123" #从表单出获得密码明文
    pwdCiphertext = desEncryption(pwdPlaintext) #password encryption

"""
处理表单函数,修改密码西信息
"""
def modifyPassword(request):
    pass

"""
处理表单函数,删除密码信息
"""
def deletePassword(request):
    pass
"""
处理表单函数,查询用户的所有密码信息
"""
def showPassword(request):
    pass

"""
返回显示登陆后的个人主页显示页面。
"""
def userIndex(request):
    pass
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

