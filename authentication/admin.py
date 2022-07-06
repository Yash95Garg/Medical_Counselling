from django.contrib import admin

# Register your models here.

from .models import *


admin.site.register(Contributor)
admin.site.register(Donator)
admin.site.register(Profile)



admin.site.register(Newsletter)
admin.site.register(Subscription)



admin.site.register(Contact)
admin.site.register(Feedback)
admin.site.register(queryModel)

admin.site.register(ShareExp)
admin.site.register(AskSuggestion)

