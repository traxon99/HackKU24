from django.db import models

class Task(models.Model):
    requester = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    task_description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
