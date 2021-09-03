from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse
from todolist.models import TaskList
from todolist.form import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def todolist(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save()
        messages.success(request, ("New Task Added!"))
        return redirect('todolist')
    else:
        all_tasks = TaskList.objects.all()
        paginator = Paginator(all_tasks, 5)
        page = request.GET.get('pg')
        all_tasks = paginator.get_page(page)
        return render(request, 'todolist.html', {'all_tasks': all_tasks})

def contact(request):
    context = {
        "welcome_text": "Welcome to Contact Us Page!"
    }
    return render(request, 'contact.html', context)

@login_required
def delete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.delete()
    return redirect('todolist')

@login_required
def complete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.done = True
    task.save()
    return redirect('todolist')

@login_required
def pending_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.done = False
    task.save()
    return redirect('todolist')

@login_required
def edit_task(request, task_id):
    if request.method == "POST":
        task_object = TaskList.objects.get(pk=task_id)
        form = TaskForm(request.POST or None, instance = task_object)
        if form.is_valid():
            form.save()
        messages.success(request, ("Task Updated!"))
        return redirect('todolist')
    else:
        task_object = TaskList.objects.get(pk=task_id)
        return render(request, 'edit.html', {'task_object': task_object})

def about(request):
    context = {
        "welcome_text": "Welcome to About Us Page!"
    }
    return render(request, 'about.html', context)

def index(request):
    context = {
        "index_text": "Welcome to Index Page!"
    }
    return render(request, 'index.html', context)