from django.contrib import admin

# Register your models here.
<<<<<<< HEAD
from .models import *

admin.site.register(Contact)
admin.site.register(Feedback)
admin.site.register(Contributor)
admin.site.register(Donator)
admin.site.register(Profile)
=======
from .models import Newsletter
from .models import Subscription
from .models import Contact
from .models import Feedback
from .models import queryModel


admin.site.register(Newsletter)
admin.site.register(Subscription)



admin.site.register(Contact)
admin.site.register(Feedback)
admin.site.register(queryModel)
>>>>>>> eb1ee43f2ed1cc0a5f0da882367f1b59690a43c4
