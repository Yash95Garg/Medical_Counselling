from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.db import models
from django.contrib.auth.models import User
from django.http import HttpResponse



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




class uniqueVisitor(models.Model):
    user = models.TextField(default=None)
    def __str__(self):
        return self.user


#DISEASE LIST 

class disease_names(models.Model):
    name = models.CharField(max_length=50)
    disease_code = models.CharField(max_length=10, blank=True, null=True)
    def save(self):
        if self.disease_code is None:
            s1 = self.name[0:3]
            s2 = str(random.randint(100,999))
            self.disease_code = s1 + s2
        super().save()



#PATHY LIST

class pathy_names(models.Model):
    name = models.CharField(max_length=50)
    pathy_code = models.CharField(max_length=10, blank=True, null=True)
    
    def save(self):
        if self.pathy_code is None:
            s1 = self.name[0:3]
            s2 = str(random.randint(100,999))
            self.pathy_code = s1 + s2
        super().save()




