from keys.models import Allkeys

def deletePasswd(tableId):
	data = Allkeys.objects.get(id=tableId)
	print(data)
	data.delete() #删除
	return "delete:ok"
