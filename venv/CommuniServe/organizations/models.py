from django.db import models

class Organization(models.Model):
    username = models.CharField(max_length=255)
    
