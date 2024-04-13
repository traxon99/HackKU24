from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('home/signup_page/', views.signup_page, name='signup_page'),
]