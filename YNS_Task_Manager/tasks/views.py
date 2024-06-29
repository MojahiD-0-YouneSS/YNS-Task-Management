from django.shortcuts import render

# Create your views here.



from .models import Task
from .forms import TaskForm, TaskEditForm

def add_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_tasks')
    else:
        form = TaskForm()
    return render(request, 'tasks/add_task.html', {'form': form})

def view_tasks(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/view_tasks.html', {'tasks': tasks})

def mark_task_as_complete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completion_status = True
    task.save()
    return redirect('view_tasks')

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('view_tasks')

def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        form = TaskEditForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('view_tasks')
    else:
        form = TaskEditForm(instance=task)
    return render(request, 'tasks/edit_task.html', {'form': form})

def search_tasks(request):
    query = request.GET.get('q')
    tasks = Task.objects.filter(name__icontains=query)
    return render(request, 'tasks/search_tasks.html', {'tasks': tasks, 'query': query})
