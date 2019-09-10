from django.db import models
from django.contrib.auth.models import User
from django.db.models import CharField

# Create your models here.


class Shops(models.Model):
	name = CharField(max_length=50)
	username = CharField(max_length=60)
	shopname = CharField(max_length=50)
	city = CharField(max_length=50)
	area = CharField(max_length=50, blank=True, null=True)
	typesport = CharField(max_length=40)

	def __str__(self):
		return f'{self.name} Shops'