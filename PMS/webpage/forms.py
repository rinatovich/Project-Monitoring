from django import forms
from .models import *


class ProjectForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = "Категория не выбрана"
        self.fields['status'].empty_label = "Статус не установлен"

        # self.fields['executor_company'].initial = [company.id for company in kwargs['instance'].executor_company.all()]
        # self.fields['manager'].initial = [manager.id for manager in kwargs['instance'].manager.all()]

    class Meta:
        model = Project
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control '}),
            'notice': forms.Textarea(attrs={'cols': 70, 'rows': 5, 'class': 'form-control'}),
            'work_statement': forms.Textarea(attrs={'class': 'form-control'}),
            'contract_id': forms.TextInput(attrs={'class': 'form-control'}),
            'customer': forms.TextInput(attrs={'class': 'form-control'}),
            'deadline': forms.DateInput(attrs={'type':'date'})
        }

    # title = forms.CharField(max_length=250)
    # work_statement = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    # contract_id = forms.CharField(max_length=250)
    # notice = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    # customer = forms.CharField(max_length=250)
    # deadline = forms.DateTimeField()
    # cat = forms.ModelChoiceField(queryset=Category.objects.all())
    # status = forms.ModelChoiceField(queryset=Status.objects.all())
    # slug = forms.SlugField(max_length=255)
    executor_company = forms.ModelMultipleChoiceField(queryset=Company.objects.all(), widget=forms.CheckboxSelectMultiple)
    manager = forms.ModelMultipleChoiceField(queryset=Manager.objects.all(), widget=forms.CheckboxSelectMultiple)
