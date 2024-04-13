from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('home/signup_page/', views.signup_page, name='signup_page'),
    path('home/organizations/', views.organizations, name='organizations'),
    path('home/organizations/signup_page/', views.signup_page, name='signup_page'),
     path('home/localevent/', views.localevent, name='localevent'),
]