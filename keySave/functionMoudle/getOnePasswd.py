from keys.models import Allkeys

def getOnePasswd(tableId):
	data = Allkeys.objects.get(id=tableId)
	return data
