from django.forms import ModelForm
from django import forms
from todolist.models import Task, Category


class DateTimePickerInput(forms.DateTimeInput):
    input_type = 'datetime-local'


class FormTask(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'

        widgets = {
            'title': forms.TextInput({'class': 'form-control'}),
            'category_id': forms.Select({'class': 'form-control'}),
            'status_id': forms.Select({'class': 'form-control'}),
            'description': forms.TextInput({'class': 'form-control'}),
            'due_date': DateTimePickerInput({'class': 'form-control'}),
        }


class FormCategory(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'name': forms.TextInput({'class': 'form-control'}),
            'description': forms.TextInput({'class': 'form-control'}),
        }
