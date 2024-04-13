from django.urls import path
from . import views

urlpatterns = [
    path('volunteers/', views.volunteers, name='volunteers'),
]