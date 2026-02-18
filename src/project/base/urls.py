from django.urls import path
from .views import PendingTasks, DetailedTask, CreateTask, UpdateTask, DeleteTask

urlpatterns = [path('', PendingTasks.as_view(), name='pending'),
               path('detailed/<int:pk>', DetailedTask.as_view(), name='detailed'),
               path('create/', CreateTask.as_view(), name='create'),
               path('update/<int:pk>', UpdateTask.as_view(), name='update'),
               path('delete/<int:pk>', DeleteTask.as_view(), name='delete'),]