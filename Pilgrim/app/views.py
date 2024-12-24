from django.shortcuts import *
from django.http import *
from django.urls import *
from django.shortcuts import *
from .models import *
from django.urls import *



def task_list(request):
    tasks = Task.objects.all() 
    return render(request, 'tasks/task_list.html', {'tasks': tasks})


def task_create(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        
        Task.objects.create(text=text)
        return redirect('task_list')
    return render(request, 'tasks/task_create.html')



