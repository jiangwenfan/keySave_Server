from django.urls import path
from keys import views

urlpatterns = [
    path('^$',views.login), #直接访问首页,走的是登录页面。
    path('^register$',views.register), #用户注册页面
    path('^showPassword$',views.showPassword), #显示所有的密码信息
    path('^addPassword$',views.addPassword), #添加密码信息
    path('^modifyPassword$',views.modifyPassword), #修改密码信息
    path('^deletePassword$',views.deletePassword), #删除密码信息
]