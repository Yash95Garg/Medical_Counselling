from django.shortcuts import render

# Create your views here.

from django.shortcuts import render,HttpResponse,redirect
from django import http

# from authentication.serializers import ShareExpSerializer

from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework.views import APIView

from django.core.mail import send_mail
from django.core.files.storage import FileSystemStorage
from .models import *
# from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
# from authentication.serializers import UserLoginSerializer



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




#SHARE EXP APIS

# @api_view(['GET','POST'])
# def shareexp(self,request,patient_no=None):
# 	if request.method == "GET":
# 		if patient_no:
# 			Exp = ShareExp.object.get(patient_no=patient_no)
# 			serializer = ShareExpSerializer(Exp)
# 			return HttpResponse(serializer.data)


# 	if request.method == "POST":
# 		serializer = ShareExpSerializer(data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return HttpResponse("<h1>Thank you for sending in your query!</h1>")
# 		else:
# 			return HttpResponse("Error")







			


    	








        


@api_view(['POST','GET'])
def Our_contributor(request):
    if request.method == 'GET':
        allContributors = Contributor.objects.all()
        context = {'allContributors': allContributors}
        return HttpResponse(allContributor)
    if request.method == 'POST':
        name = request.data.get('name')
        uploaded_file=request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        imageurl = fs.url(name)
        about = request.POST.get('about')
        status = request.POST.get('status')
        Facebook_url = request.POST.get('Facebook_url')
        Instagram_url = request.POST.get('Instagram_url')
        Mail_url = request.POST.get('Mail_url')
        Twitter_url = request.POST.get('Twitter_url')
        contributor_obj = Contributor(
            name=name,
            Facebook_url = Facebook_url,
            Instagram_url = Instagram_url,
            Mail_url = Mail_url,
            Twitter_url = Twitter_url,
            about = about,
            status = status, imageurl = imageurl
            )
        contributor_obj.save()
        print(contributor_obj)
        return HttpResponse("Added")

@api_view(['POST', 'GET'])
def our_donator(request):
    if request.method == 'POST':
        name = request.data.get('name')
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        imageurl = fs.url(name)
        about = request.POST.get('about')
        status = request.POST.get('status')
        Facebook_url = request.POST.get('Facebook_url')
        Instagram_url = request.POST.get('Instagram_url')
        Mail_url = request.POST.get('Mail_url')
        Twitter_url = request.POST.get('Twitter_url')


        donator_obj = Donator(
            name = name,
            about = about,
            Facebook_url=Facebook_url,
            Instagram_url=Instagram_url,
            Mail_url=Mail_url,
            Twitter_url=Twitter_url,
            status = status, imageurl = imageurl
            )
        donator_obj.save()
        print(donator_obj)
        return HttpResponse("Added successfully")
    if request.method == 'GET':
        allDonators = Donators.objects.all()
        context = {'allDonators': allDonators}
        return HttpResponse(allDonators)



@api_view(['GET', 'POST'])
def FbLogin(request):
	if request.method == "GET":
		allFbLogin=FbLogin.objects.all()
		context={'FbLogin': FbLogin}
		return HttpResponse(FbLogin)
	if request.method == "POST":
		name = request.POST.get('name')
		email = request.POST.get('email')
		Fblogin_obj = Contact(
			name = name,
			email = email,
		)
		Fblogin_obj.save()
		return HttpResponse("Succesfully Logged In via Facebook.")

