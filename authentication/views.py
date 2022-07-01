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




#test

#CONTACT PAGE
@api_view(['GET', 'POST'])
def Contacts(request):
	if request.method == "GET":
		allContacts=Contact.objects.all()
		context={'allContacts': allContacts}
		return HttpResponse(allContacts)
	if request.method == "POST":
		name = request.POST.get('name')
		email = request.POST.get('email')
		subject = request.POST.get('subject')
		contact_obj = Contact(
			name = name,
			email = email,
			subject = subject,
		)
		contact_obj.save()
		return HttpResponse("Query received.")


#FEEDBACK FORM
@api_view(['GET', 'POST'])
def feedback(request):
	if request.method == "GET":
		allfeedback=Feedback.objects.all()
		context={'allfeedback': allfeedback}
		return HttpResponse(allfeedback)
	if request.method == "POST":
		feedback = Feedback()
		name = request.POST.get('name')
		email = request.POST.get('email')
		subject = request.POST.get('subject')
		feedback.name = name
		feedback.email = email
		feedback.subject = subject
		feedback.save()
		return HttpResponse("<h1>Thank you for your feedback!</h1>")

#RAISE A QUERY
@api_view(['GET', 'POST'])
def raiseaquery(request):
	if request.method == "GET":
		allquery=queryModel.objects.all()
		context={'allquery': allquery}
		return HttpResponse(allquery)
	if request.method == "POST":
		query = queryModel()
		name = request.POST.get('name')
		email = request.POST.get('email')
		subject = request.POST.get('subject')
		query.name = name
		query.email = email
		query.subject = subject
		query.save()
		return HttpResponse("<h1>Thank you for sending in your query!</h1>")
