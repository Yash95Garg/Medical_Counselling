from django.urls import path
from . import views

urlpatterns = [
    path('y', views.newsletterHome),
    path('ex/', views.newsletterHome)

]