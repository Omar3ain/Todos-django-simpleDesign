from django.forms import CheckboxInput, TextInput
import django_filters
from django_filters import CharFilter
from .models import Todo

class TodoFilter(django_filters.FilterSet):
    title = CharFilter(field_name = "title", lookup_expr = "icontains")
    createdAt = CharFilter(field_name = "createdAt", lookup_expr="year")
    createdAt__gt = CharFilter(field_name = "createdAt", lookup_expr="year__gt")
    createdAt__lt = CharFilter(field_name = "createdAt", lookup_expr="year__lt")

    class Meta:
        model = Todo
        fields = '__all__'
        exclude = ['user']
        widgets = {
            'title': TextInput(attrs={
            'class': 'form-control',
            }),
            'is_completed': CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }