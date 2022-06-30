from django.contrib import admin

# Register your models here.

from .models import Contact
from .models import Feedback

admin.site.register(Contact)
admin.site.register(Feedback)