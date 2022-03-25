from django.urls import path
from api import views

urlpatterns = [
    path('add',views.addPasswd),
	path('select',views.selectPasswd),
	path('modify',views.modifyPasswd),
	path('delete',views.deletePasswd),
]
