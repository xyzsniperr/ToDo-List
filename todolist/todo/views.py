from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json
from .models import Task, List

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def list_list(request):
    lists = List.objects.filter(user=request.user)
    list_data = []
    for lst in lists:
        open_tasks = lst.tasks.filter(completed=False).count()
        completed_tasks = lst.tasks.filter(completed=True).count()
        list_data.append({
            'list': lst,
            'open_tasks': open_tasks,
            'completed_tasks': completed_tasks,
        })
    
    return render(request, 'list_list.html', {'list_data': list_data})

@login_required
def list_create(request):
    if request.method == 'POST':
        list_name = request.POST.get('name')
        if list_name:
            new_list = List(name=list_name, user=request.user)
            new_list.save()
            return redirect('list_list')
    return redirect('list_list')

@login_required
def list_delete(request, list_id):
    list = get_object_or_404(List, id=list_id, user=request.user)
    if request.method == 'POST':
        print('delete')
        list.delete()
        return redirect('/')
    return render(request, 'list_list.html', {'lists': List.objects.all()})

@login_required
def task_list(request, list_id):
    list = get_object_or_404(List, id=list_id, user=request.user)
    tasks = list.tasks.all()
    return render(request, 'task_list.html', {'list': list, 'tasks': tasks})

@login_required
def task_create(request, list_id):
    list = get_object_or_404(List, id=list_id, user=request.user)
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description', '')
        completed = 'completed' in request.POST

        new_task = Task(
            list=list,
            title=title,
            description=description,
            completed=completed
        )
        new_task.save()
        return redirect('task_list', list_id=list.id)

    return render(request, 'task_form.html', {'list': list})

@login_required
def task_update(request, list_id, pk):
    list = get_object_or_404(List, id=list_id, user=request.user)
    task = get_object_or_404(Task, list=list, pk=pk)

    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.completed = 'completed' in request.POST
        task.save()
        return redirect('task_list', list_id=list.id)

    return render(request, 'task_list.html', {'list': list, 'task': task})

@login_required
def task_delete(request, list_id, pk):
    list = get_object_or_404(List, id=list_id, user=request.user)
    task = get_object_or_404(Task, list=list, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list', list_id=list.id)
    return render(request, 'task_confirm_delete.html', {'task': task, 'list': list})

@login_required
def update_task_status(request, task_id):
    if request.method == 'POST':
        task = get_object_or_404(Task, pk=task_id, list__user=request.user)
        data = json.loads(request.body)
        task.completed = data['completed']
        task.save()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False}, status=400)