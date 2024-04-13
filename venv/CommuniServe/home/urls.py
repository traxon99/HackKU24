from django.urls import path
from . import views
from tasks.views import task_list  # Import the task_list view from the other app


urlpatterns = [
    path('', views.home, name='home' ),
    path('signup_page/', views.signup_page, name='signup_page'),
    path('organizations/', views.organizations, name='organizations'),
    path('organizations/signup_page/', views.signup_page, name='signup_page'),
    path('localevent/', views.localevent, name='localevent'),
]
