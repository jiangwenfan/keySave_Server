from django.shortcuts import render
from functionMoudle.savePasswd import savePasswd
"""

1.根据不同响应方式返回不同的页面。
2.获取表单的提交数据，提交给addPasswd函数
3.根据返回值返回不同的响应页面
"""
def addHandle(request):
    if request.method == 'GET':
        return render(request, 'keys/add.html')
    else:
        data = {}
        data['siteId'] = request.POST.get('siteId')
        data['sitePasswdEncry'] = request.POST.get('sitePasswdEncry')
        data['siteName'] = request.POST.get('siteName')
        data['siteDomain'] = request.POST.get('siteDomain')
        data['siteLoginUrl'] = request.POST.get('siteLoginUrl')
        data['siteLoginArea'] = request.POST.get('siteLoginArea')
        data['algor'] = request.POST.get('algor')
        print(data)

        if savePasswd(data):
            return render(request, 'keys/addRes.html', {'status': '添加Ok'})
        else:
            return render(request, 'keys/addRes.html', {'status': '添加error'})
