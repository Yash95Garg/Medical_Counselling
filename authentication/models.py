from platform import mac_ver
from random import random
from django.db import models
from django.contrib.auth.models import (
    User, AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.db import models
from django.contrib.auth.models import User
from django.http import HttpResponse

import random


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
#WEEK2 TASKs


#share_experiance model

class ShareExp(models.Model):
    username = models.ForeignKey(User, on_delete= models.CASCADE)
    patient_name = models.CharField(max_length=20)
    GENDER_CHOICES = (
        ('M','Male'),
        ('F','Female'),
        ('O','Others'),
    )
    gender = models.CharField(max_length=10,choices=GENDER_CHOICES)
    age = models.IntegerField(max_length=3)
    phone = models.IntegerField(max_length=10)
    email = models.CharField(max_length=50)
    disease_name = models.CharField(max_length=50)
    pathy_name = models.CharField(max_length=50)
    
    description = models.CharField(max_length=255)
    additional_file_url = models.CharField(max_length=50)

    VERIFICATION = (
        ('V', 'Verified'),
        ('U', 'Unverified'),
    )
    verification = models.TextField(max_length=10, choices=VERIFICATION)

    Status = (
        ('E', 'Enabled'),
        ('D', 'Disabled'),
    )
    status = models.TextField(max_length=10, choices=Status)

    RATING = (
        ('1', 'VeryBad'),
        ('2', 'Bad'),
        ('3', 'Okay'),
        ('4', 'Good'),
        ('5', 'Excellent'),
    )
    ratings = models.IntegerField(default=3, choices=RATING)


    case_no = models.IntegerField(max_length=5)
    title = models.CharField(max_length=50)


#Ask suggestion model

class AskSuggestion(models.Model):
    username = models.ForeignKey(User, on_delete= models.CASCADE)
    patient_name = models.CharField(max_length=20)
    
    GENDER_CHOICES = (
        ('M','Male'),
        ('F','Female'),
        ('O','Others'),
    )
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES)
    age = models.IntegerField(max_length=3)
    phone = models.IntegerField(max_length=10)
    email = models.CharField(max_length=50)
    disease_name = models.CharField(max_length=50)
    symptoms = models.CharField(max_length=255)
    
    description = models.CharField(max_length=255)
    additional_file_url = models.CharField(max_length=50)

    current_condition = models.CharField(max_length=255)
    query = models.CharField(max_length=255)

    case_no = models.IntegerField(max_length=5)
    title = models.CharField(max_length=50)

 

#user profile model

class Profile(models.Model):
	user = models.ForeignKey(User, on_delete= models.CASCADE, blank=True, null=True)
	Profile_Pic = models.CharField(default='False', max_length=200)
	UserType = (
	('A', 'Admin'),
	('U', 'User'),
	)
	usertype = models.CharField(default='U', max_length=1, choices=UserType)
	GENDER_CHOICES = (
		('M', 'Male'),
		('F', 'Female'),
		('Other', 'Other'),
	)
	gender = models.CharField(max_length=5, choices=GENDER_CHOICES, blank=True, null=True)
	Age = models.IntegerField(blank=True, null=True)
	Mobile_Number = models.IntegerField(blank=True, null=True)




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




    
