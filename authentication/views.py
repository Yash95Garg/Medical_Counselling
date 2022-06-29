from django.shortcuts import render

# Create your views here.

from django.shortcuts import render,HttpResponse,redirect
from django import http
from rest_framework.decorators import api_view
from django.contrib.auth.models import User

from django.core.mail import send_mail
from django.core.files.storage import FileSystemStorage
from .models import *





#newsletter database apis
@api_view(['POST'])
def add_newsletter(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
    fs = FileSystemStorage()
    name = fs.save(uploaded_file.name, uploaded_file)
    imageurl = fs.url(name)
    title = request.POST.get('title')
    description = request.POST.get('description')
    
    
    newsletter_obj = Newsletter(
        title = title, 
        description = description, imageurl = imageurl
        )
    newsletter_obj.save()
    

    print(newsletter_obj)
    return HttpResponse("Added")


@api_view(['GET'])
def newsletterHome(request): 
    allLetters=Newsletter.objects.all()
    context={'allLetters': allLetters} 
    return HttpResponse(allLetters)
    


#subscription apis 
@api_view(['POST'])
def register(request):
    email = request.data.get('email')   
    name = request.data.get('name')
    if Subscription.objects.filter(email = email).first():
        return HttpResponse("Email Already Exists")   
    sub_obj = Subscription.objects.create_sub(email=email, name = name)     
    sub_obj.save()
    send_mail_after_subscription(email)
    return HttpResponse("Subscription Added Succesfully")




def send_mail_after_subscription(email):
    subject = 'Monthly Newsletter'
    message = f'SUBSCRIPTION CONFIRMED'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message , email_from ,recipient_list )	