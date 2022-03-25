from django.urls import path
from keys import views

urlpatterns = [
    #path('^$',views.login), #直接访问首页,走的是登录页面。
    #path('^register$',views.register), #用户注册页面
    path('select',views.selectPasswd), #显示所有的密码信息
    path('add',views.addPasswd), #添加密码信息
    path('modify',views.modifyPasswd), #修改密码信息
    path('delete',views.deletePasswd), #删除密码信息
	path('show',views.userIndex),
]
