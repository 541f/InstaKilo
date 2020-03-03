from django.db import models

class signup(models.Model):
	email= models.CharField(max_length=40, null=True, blank=True)
	fullname= models.CharField(max_length=40, null=True, blank=True)
	username= models.CharField(max_length=40, null=True, blank=True)
	password= models.CharField(max_length=40, null=True, blank=True)
	dp= models.ImageField()

	def __str__(self):
		return self.username

class post(models.Model):
	username= models.CharField(max_length=40, null=True, blank=True)
	postid= models.CharField(max_length=40, null=True, blank=True)
	images= models.ImageField()
	

	def __str__(self):
		return self.username + '==>' + self.postid + '==>' + self.images

# Create your models here.
