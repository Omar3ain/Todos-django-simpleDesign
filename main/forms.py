from django.forms import ModelForm, TextInput
from .models import Todo,TodoItems

class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
            })
        }

class TodoItemsForm(ModelForm):
    class Meta:
        model = TodoItems
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
            })
        }
