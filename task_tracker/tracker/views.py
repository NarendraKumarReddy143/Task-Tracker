from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import TaskForm

def task_create(request):
    form = TaskForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('success')
    return render(request, 'task_form.html', {'form': form})

def success(request):
    return render(request, 'success.html')
