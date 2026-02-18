from django import forms
from .models import Task
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'input', 'placeholder': 'e.g., Buy groceries'}),
            'description': forms.Textarea(attrs={'class': 'input', 'rows': 4, 'placeholder': 'Optional notes...'}),
            'completed': forms.CheckboxInput(),
        }

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input'}))

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']
        widgets = {
            'username': forms.TextInput(attrs={'class':'input'}),
        }