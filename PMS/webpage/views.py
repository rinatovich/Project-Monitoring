from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import FormView, CreateView, ListView
from rest_framework import generics

from .forms import AddProjectForm
from .models import *
from django import forms
from openpyxl import load_workbook
from .admin import ProjectResource

# Create your views here.
from .serializers import ProjectSerializer, CategorySerializer
from .utils import DataMixin

menu = [{'text': 'Изменить', 'url': '/admin/webpage/project/'}, ]

cats = Category.objects.all()
for c in cats:
    menu.append({'text': c.title, 'url': f'/category/{c.slug}'})

fields = {
    'stroitelno-montazhnye-raboty': ['№', 'Наименование объекта', 'Описание работ', '№ договора', 'Примечание',
                                     'Заказчик', 'Ответственная организация', 'Ответственный на месте', 'Статус',
                                     'Срок'],
    'proektnye-raboty': ['№', 'Наименование объекта', 'Описание работ', '№ договора', 'Примечание',
                         'Заказчик', 'Ответственная организация', 'Ответственный на месте', 'Статус',
                         'Срок'],
    'teh-obsluzhivanie': ['№', 'Наименование Объекта', 'Описание работ', '№ договора', 'Примечание', 'Заказчик',
                          'Ответственная организация', 'Ответственный на месте', 'Статус'],
    'raboty-po-zaprosu': ['№', 'Наименование работ', 'Описание работ', '№ договора', 'Примечание', 'Заказчик',
                          'Ответственный на месте', 'Статус', 'Срок']
}


def index(request):
    # projects = Project.objects.all()
    # status = Status.objects.all()
    # for project in projects:
    #         if project.status is None:
    #             project.status_id = 1
    #             project.save()
    return redirect('category/stroitelno-montazhnye-raboty')


def shutdown(request):
    return render(request, 'webpage/shutdown.html')


class add(CreateView):
    template_name = 'webpage/add.html'
    success_url = '/'
    form_class = AddProjectForm


class ProjectCategory(DataMixin, ListView):
    model = Project
    template_name = 'webpage/index.html'
    context_object_name = 'projects'

    def get_queryset(self):
        return Project.objects.filter(cat__slug=self.kwargs['cat_slug']).select_related('cat')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['iter'] = 1
        c = Category.objects.get(slug=self.kwargs['cat_slug'])
        context['category'] = c
        c_def = self.get_user_context(title='Category - ' + str(c.title),
                                      cat_selected=c.pk)
        return dict(list(context.items()) + list(c_def.items()))


class ProjectAPIView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
