from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Task


def index(request):
    tasks = Task.objects.all()
    return render(request, 'todo/index.html', {'tasks': tasks})


def add_task(request):
    if request.method == 'POST':
        # دریافت مقدار انتخاب شده از select

        selected_option = request.POST.get('task_type')
        selected_title = request.POST.get('title')
        if selected_option:
            Task.objects.create(title=selected_title, tag=selected_option)
    return render(request, 'todo/add_task.html')


def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('index')


def edit(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        savechange(request, task_id)
        return redirect('http://127.0.0.1:8000/')
    else:
        return render(request, 'todo/task.html', {'task': task})


def savechange(request, task_id):
    selected_option = request.POST.get('task_type')
    selected_title = request.POST.get('title')
    print(selected_title, selected_option)
    task = Task.objects.get(id=task_id)
    task.title = selected_title
    task.tag = selected_option
    task.save()


