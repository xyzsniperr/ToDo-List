from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, List
from .forms import TaskForm

def list_list(request):
    lists = List.objects.all()
    return render(request, 'list_list.html', {'lists': lists})

def list_create(request):
    if request.method == 'POST':
        list_name = request.POST.get('name')
        if list_name:
            new_list = List(name=list_name)
            new_list.save()
            return redirect('list_list')
    return redirect('list_list')

def list_delete(request, list_id):
    list = get_object_or_404(List, id=list_id)
    if request.method == 'POST':
        print('delete')
        list.delete()
        return redirect('/')
    return render(request, 'list_list.html', {'lists': List.objects.all()})

def task_list(request, list_id):
    list = get_object_or_404(List, id=list_id)
    tasks = list.tasks.all()
    return render(request, 'task_list.html', {'list': list, 'tasks': tasks})

def task_create(request, list_id):
    list_ = get_object_or_404(List, id=list_id)
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description', '')
        completed = 'completed' in request.POST

        new_task = Task(
            list=list_,
            title=title,
            description=description,
            completed=completed
        )
        new_task.save()
        return redirect('task_list', list_id=list_.id)

    return render(request, 'task_form.html', {'list': list_})
def task_update(request, list_id, pk):
    list_ = get_object_or_404(List, id=list_id)
    task = get_object_or_404(Task, list=list_, pk=pk)

    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.completed = 'completed' in request.POST
        task.save()
        return redirect('task_list', list_id=list_.id)

    return render(request, 'task_list.html', {'list': list_, 'task': task})


def task_delete(request, list_id, pk):
    list = get_object_or_404(List, id=list_id)
    task = get_object_or_404(Task, list=list, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list', list_id=list.id)
    return render(request, 'task_confirm_delete.html', {'task': task, 'list': list})
