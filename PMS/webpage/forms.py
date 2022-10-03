from django import forms
from .models import *


class AddProjectForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['executor_company'].checked = 1

    executor_company = forms.ModelMultipleChoiceField(
        queryset=Company.objects.all(),
        widget=forms.CheckboxSelectMultiple)
    manager = forms.ModelMultipleChoiceField(
        queryset=Manager.objects.all(),
        widget=forms.CheckboxSelectMultiple)


    class Meta:
        model = Project
        fields = [field.name for field in Project._meta.fields]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10})
        }
