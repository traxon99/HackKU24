from django.db import models

class Volunteer(models.Model):
    username = models.CharField(max_length=255)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    
