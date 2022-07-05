from django.urls import path, include
from . import views

urlpatterns = [
    path('y', views.newsletterHome),
    path('ex/', views.newsletterHome),
    path('contact/', views.Contacts, name = 'contact'),
    path('feedback/', views.feedback, name = 'feedback'),
<<<<<<< HEAD
    path('contributors/', views.Our_contributor),
    path('donators/', views.our_donator),
    # path('login/', views.UserLoginView),

=======
    path('query/', views.raiseaquery, name = 'query'),
   
    
>>>>>>> eb1ee43f2ed1cc0a5f0da882367f1b59690a43c4
]