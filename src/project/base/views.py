from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Task

class PendingTasks(ListView):
    model = Task
    context_object_name = 'tasks'

class DetailedTask(DetailView):
    model = Task
    template_name = 'base/detailed_task.html'
    context_object_name = 'task'

class CreateTask(CreateView):
    model = Task
    fields = '__all__'
    template_name = 'base/task_form.html'
    context_object_name = 'task'
    success_url = reverse_lazy('pending')

class UpdateTask(UpdateView):
    model = Task
    fields = '__all__'
    template_name = 'base/task_update.html'
    context_object_name = 'task'
    success_url = reverse_lazy('pending')

class DeleteTask(DeleteView):
    model = Task
    template_name = 'base/task_delete.html'
    context_object_name = 'task'
    success_url = reverse_lazy('pending')