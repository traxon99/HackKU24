from django.http import HttpResponse
from django.template import loader
from tasks.models import Task  # Import the Task model from the other app
from django.shortcuts import render

def home(request):
    # Retrieve tasks from the database
    tasks = Task.objects.all()

    # Pass tasks data to the template
    return render(request, 'home.html', {'tasks': tasks})

def signup_page(request):
  template = loader.get_template('signup_page.html')
  return HttpResponse(template.render())

def organizations(request):
  template = loader.get_template('organizations.html')
  return HttpResponse(template.render())

def localevent(request):
  template = loader.get_template('localevent.html')
  return HttpResponse(template.render())

def login(request):
  template = loader.get_template('login.html')
  return HttpResponse(template.render())
