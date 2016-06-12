from __future__ import unicode_literals

from django.db import models

class TestModule(models.Model):
	module_name = models.CharField(max_length=50,db_index=True)
	path = models.CharField(max_length=1000,default=0)
	module_desc = models.CharField(max_length=200,blank=True)
	create_date = models.DateTimeField(auto_now_add=True)

class User(models.Model):
    username = models.CharField(max_length=50,db_index=True)
    password = models.CharField(max_length=50)
    email = models.EmailField(default="")


