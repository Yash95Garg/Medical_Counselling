from django.contrib import admin

# Register your models here.
from .models import Newsletter
from .models import Subscription
from .models import Contact
from .models import Feedback
from .models import queryModel
from .models import uniqueVisitor

from .models import *


admin.site.register(Contributor)
admin.site.register(Donator)
admin.site.register(Profile)



admin.site.register(Newsletter)
admin.site.register(Subscription)



admin.site.register(Contact)
admin.site.register(Feedback)
admin.site.register(queryModel)


admin.site.register(uniqueVisitor)
admin.site.register(ShareExp)
admin.site.register(AskSuggestion)

admin.site.register(disease_names)
admin.site.register(pathy_names)
