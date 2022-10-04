from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms import DateField

from .models import *
from PMS import settings


class DateInput(forms.DateInput):
    input_type = 'date'


class ProjectForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = "Категория не выбрана"
        self.fields['status'].empty_label = "Статус не установлен"

    class Meta:
        model = Project
        fields = '__all__'
        exclude = ('note',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control '}),
            'notice': forms.Textarea(attrs={'cols': 70, 'rows': 5, 'class': 'form-control'}),
            'work_statement': forms.Textarea(attrs={'class': 'form-control'}),
            'contract_id': forms.TextInput(attrs={'class': 'form-control'}),
            'customer': forms.TextInput(attrs={'class': 'form-control'}),
            'deadline': DateInput(format=('%Y-%m-%d'))
        }

    executor_company = forms.ModelMultipleChoiceField(queryset=Company.objects.all(), widget=forms.CheckboxSelectMultiple, label="Исполняющая организация")
    manager = forms.ModelMultipleChoiceField(queryset=Manager.objects.all(), widget=forms.CheckboxSelectMultiple, label="Ответственные лица")


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class NoteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Note
        fields = ['text']
        widgets = {
            'text': forms.TextInput(attrs={'class': 'form-control '}),
        }
