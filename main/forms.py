from django import forms
from .models import Todo,TodoItems
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
            })
        }

class TodoItemsForm(forms.ModelForm):
    class Meta:
        model = TodoItems
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
            })
        }
class userCreation(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
            'class': 'form-control',
            'style': 'width: 50%;',
            }),
            'email': forms.TextInput(attrs={
            'class': 'form-control',
            'style': 'width: 50%;',
            }),
            'password1': forms.PasswordInput(attrs={
            'class': 'form-control',
            'style': 'width: 50%;',
            }),
            'password2': forms.PasswordInput(attrs={
            'class': 'form-control',
            'style': 'width: 50%;',
            }),
        }