from django.urls import path
from . import views
from tasks.views import task_list  # Import the task_list view from the other app


urlpatterns = [
    path('home/', views.home, name='home'),
    path('home/signup_page/', views.signup_page, name='signup_page'),
    path('tasks/', task_list, name='task_list'),
    path('home/organizations/', views.organizations, name='organizations'),
    path('home/organizations/signup_page/', views.signup_page, name='signup_page'),
    path('home/localevent/', views.localevent, name='localevent'),
]
