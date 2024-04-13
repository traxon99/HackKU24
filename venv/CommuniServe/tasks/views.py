from django.shortcuts import render
from .models import Task

def task_list(request):
    # Retrieve tasks from the database
    tasks = Task.objects.all()

    # Pass tasks data to the template
    return render(request, 'task_list.html', {'tasks': tasks})
