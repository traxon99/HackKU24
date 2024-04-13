from django.http import HttpResponse
from django.template import loader

def home(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())

def signup_page(request):
  template = loader.get_template('signup_page.html')
  return HttpResponse(template.render())

def organizations(request):
  template = loader.get_template('organizations.html')
  return HttpResponse(template.render())

def localevent(request):
  template = loader.get_template('localevent.html')
  return HttpResponse(template.render())