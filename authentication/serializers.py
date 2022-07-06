# from dataclasses import fields
# from rest_framework import serializers
# from .models import ShareExp , AskSuggestion
# from django.contrib.auth.models import User

# #SHARE EXPERIANCE SERIALIZER

# class ShareExpSerializer(serializers.ModelSerializer):
#     username = serializers.CharField(source='User.username')
#     patient_name = serializers.CharField(max_length=20,required= True)
    
#     GENDER_CHOICES = (
#         ('M','Male'),
#         ('F','Female'),
#         ('O','Others'),
#     )
#     gender = serializers.CharField(max_length=1,choices=GENDER_CHOICES)
#     age = serializers.IntegerField(max_length=3)
#     phone = serializers.IntegerField(max_length=10)
#     email = serializers.CharField(max_length=50)
#     disease_name = serializers.CharField(max_length=50)
#     pathy_name = serializers.CharField(max_length=50)
#     description = serializers.CharField(max_length=255)
#     additional_file_url = serializers.CharField(max_length=50)

#     VERIFICATION = (
#         ('V', 'Verified'),
#         ('U', 'Unverified'),
#     )
#     verification = serializers.TextField(max_length=10, choices=VERIFICATION)

#     Status = (
#         ('E', 'Enabled'),
#         ('D', 'Disabled'),
#     )
#     status = serializers.TextField(max_length=10, choices=Status)

#     RATING = (
#         ('1', 'VeryBad'),
#         ('2', 'Bad'),
#         ('3', 'Okay'),
#         ('4', 'Good'),
#         ('5', 'Excellent'),
#     )
#     ratings = serializers.IntegerField(default=3, choices=RATING)


#     case_no = serializers.IntegerField(max_length=5)
#     title = serializers.CharField(max_length=50)

#     class Meta:
#         model = ShareExp
#         fields = ('__all__')


