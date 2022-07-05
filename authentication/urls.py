from django.urls import path
from . import views

urlpatterns = [
    path('y', views.newsletterHome),
    path('ex/', views.newsletterHome),
    path('contact/', views.Contacts, name = 'contact'),
    path('feedback/', views.feedback, name = 'feedback'),
    path('contributors/', views.Our_contributor),
    path('donators/', views.our_donator),
    # path('login/', views.UserLoginView),

]