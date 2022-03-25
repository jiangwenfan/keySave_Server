# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#	* Rearrange models' order
#	* Make sure each model has one field with primary_key=True
#	* Make sure each ForeignKey has `on_delete` set to the desired behavior.
#	* Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Allkeys(models.Model):
	userName = models.CharField(db_column='userName', max_length=200, blank=True, null=True)  # Field name made lowercase.
	userPasswd = models.CharField(db_column='userPasswd', max_length=300, blank=True, null=True)  # Field name made lowercase.
	siteId = models.CharField(max_length=255, blank=True, null=True)
	sitePasswdEncry = models.CharField(db_column='sitePasswdEncry', max_length=1000, blank=True, null=True)  # Field name made lowercase.
	siteName = models.CharField(db_column='siteName', max_length=255, blank=True, null=True)  # Field name made lowercase.
	siteDomain = models.CharField(db_column='siteDomain', max_length=500, blank=True, null=True)  # Field name made lowercase.
	siteLoginUrl = models.CharField(db_column='siteLoginUrl', max_length=1000, blank=True, null=True)  # Field name made lowercase.
	siteLoginArea = models.CharField(db_column='siteLoginArea', max_length=250, blank=True, null=True)	# Field name made lowercase.
	key = models.CharField(max_length=255, blank=True, null=True)
	algor = models.CharField(max_length=255, blank=True, null=True)

	class Meta:
		managed = False
		db_table = 'allKeys'
