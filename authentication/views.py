from django.shortcuts import render

# Create your views here.

from django.shortcuts import render,HttpResponse,redirect
from django import http
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework.views import APIView

from django.core.mail import send_mail
from django.core.files.storage import FileSystemStorage
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken
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

# class UserLoginView(APIView):
#     # renderer_classes = [UserRenderer]
#     def post(self, request, format=None):
#         serializer = UserLoginSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         email = serializer.data.get('email')
#         password = serializer.data.get('password')
#         user = authenticate(email=email, password=password)
#         if user is not None:
#             token = get_tokens_for_user(user)
#             return Response({'token':token, 'msg':'Login Success'}, status=status.HTTP_200_OK)
#         else:
#             return Response({'errors':{'non_field_errors':['Email or Password is not Valid']}}, status=status.HTTP_404_NOT_FOUND)

