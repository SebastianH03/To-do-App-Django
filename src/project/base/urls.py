from django.urls import path
from .views import PendingTasks, DetailedTask, CreateTask, UpdateTask, DeleteTask, Login, Register
from django.contrib.auth.views import LogoutView

urlpatterns = [path('', PendingTasks.as_view(), name='pending'),
               path('login/', Login.as_view(), name='login'),
               path('register/', Register.as_view(), name='register'),
               path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
               path('detailed/<int:pk>/', DetailedTask.as_view(), name='detailed'),
               path('create/', CreateTask.as_view(), name='create'),
               path('update/<int:pk>/', UpdateTask.as_view(), name='update'),
               path('delete/<int:pk>/', DeleteTask.as_view(), name='delete'),]