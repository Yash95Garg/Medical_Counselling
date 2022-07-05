# from rest_framework import serializers
# from authentication.models import User
# from django.utils.encoding import smart_str, force_bytes, DjangoUnicodeDecodeError
# from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
# from django.contrib.auth.tokens import PasswordResetTokenGenerator
# # from authentication.utils import Util
# class UserLoginSerializer(serializers.ModelSerializer):
#   email = serializers.EmailField(max_length=255)
#   class Meta:
#     model = User
#     fields = ['email', 'password']