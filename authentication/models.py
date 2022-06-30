from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.db import models




class Newsletter(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    imageurl = models.CharField(default='False', max_length=200)
    
    


class Subscription(models.Model):
    
    email = models.EmailField(max_length=50)
    name = models.TextField()


class Contact(models.Model):
	name = models.CharField(max_length=150)
	email = models.EmailField()
	subject = models.TextField()
	def __str__(self):
		return self.name 


class Feedback(models.Model):
	name = models.CharField(max_length=150)
	email = models.EmailField()
	subject = models.TextField()
	def __str__(self):
		return self.name 
		


class queryModel(models.Model):
	name = models.CharField(max_length=150)
	email = models.EmailField()
	subject = models.TextField()
	def __str__(self):
		return self.name 

class Contributor(models.Model):
    Name = models.CharField(max_length=20)
    Imageurl = models.CharField(default='False', max_length=200)
    About = models.TextField(max_length=500)
    Status = (
        ('A', 'Active'),
        ('I', 'Inactive'),
    )
    status = models.CharField(max_length=10, choices=Status)
    Facebook_url = models.TextField(max_length=50)
    Instagram_url = models.TextField(max_length=50)
    Mail_url = models.TextField(max_length=50)
    Twitter_url = models.TextField(max_length=50)

class Donator(models.Model):
    Name = models.TextField(max_length=20)
    Imageurl = models.CharField(default='False', max_length=200)
    About = models.TextField(max_length=200)
    Status = (
        ('A', 'Active'),
        ('I', 'Inactive'),
    )
    status = models.TextField(max_length=10, choices=Status)
    Facebook_url = models.TextField(max_length=50)
    Instagram_url = models.TextField(max_length=50)
    Mail_url = models.TextField(max_length=50)
    Twitter_url = models.TextField(max_length=50)
