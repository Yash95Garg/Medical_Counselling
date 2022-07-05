from platform import mac_ver
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.db import models
from django.contrib.auth.models import User



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

 
