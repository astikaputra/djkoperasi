from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

status_choice=(
		(0,'Non Aktif'),
		(1,'Aktif'),
	)
User = get_user_model()

class Category(models.Model):
	code=models.CharField(max_length=10)
	name=models.CharField(max_length=30)
	icon=models.ImageField()
	status=models.IntegerField(choices=status_choice)

	def __str__(self):
		return self.code

class Modul(models.Model):
	modul_code=models.CharField(max_length=10)
	name=models.CharField(max_length=30)
	icon=models.ImageField()
	url=models.SlugField()
	categories=models.ForeignKey(Category, on_delete=models.CASCADE)
	status=models.IntegerField(choices=status_choice)

	def __str__(self):
		return self.modul_code

class AssignModul(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    modul = models.ManyToManyField(Modul)

