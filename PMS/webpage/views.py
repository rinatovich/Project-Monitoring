from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, ListView, UpdateView
from .forms import ProjectForm
from .models import *
from .utils import DataMixin

# menu settings
menu = [{'text': 'Изменить', 'url': '/admin/webpage/project/'},
        {'text': 'Добавить', 'url': '/project/add'}]
cats = Category.objects.all()
for c in cats:
    menu.append({'text': c.title, 'url': f'/category/{c.slug}'})


def index(request):
    return redirect('category/stroitelno-montazhnye-raboty')


class ProjectCategory(DataMixin, ListView):
    model = Project
    template_name = 'webpage/index.html'
    context_object_name = 'projects'
    active_manager = None
    active_company = None

    def get_queryset(self):
        if self.request.GET:
            print(self.request.GET)
            if all(k in self.request.GET for k in ('manager', 'company')):
                managers = self.request.GET['manager'].split(',')
                self.active_manager = Manager.objects.filter(id__in=managers)
                companies = self.request.GET['company'].split(',')
                self.active_company = Company.objects.filter(id__in=companies)
                return Project.objects.filter(cat__slug=self.kwargs['cat_slug'], manager__pk__in=managers,
                                              executor_company__pk__in=companies).select_related('cat')
            elif 'company' in self.request.GET:
                companies = self.request.GET['company'].split(',')
                self.active_company = Company.objects.filter(id__in=companies)
                return Project.objects.filter(cat__slug=self.kwargs['cat_slug'],
                                              executor_company__pk__in=companies).select_related('cat')
            elif 'manager' in self.request.GET:
                managers = self.request.GET['manager'].split(',')
                self.active_manager = Manager.objects.filter(id__in=managers)
                return Project.objects.filter(cat__slug=self.kwargs['cat_slug'],
                                              manager__pk__in=managers).select_related('cat')
        else:
            return Project.objects.filter(cat__slug=self.kwargs['cat_slug']).select_related('cat')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.active_manager:
            context['active_manager'] = self.active_manager
        if self.active_company:
            context['active_company'] = self.active_company
        context['iter'] = 1
        context['managers'] = Manager.objects.all()
        context['companies'] = Company.objects.all()
        categories = Category.objects.get(slug=self.kwargs['cat_slug'])
        context['category'] = categories
        c_def = self.get_user_context(title='Category - ' + str(c.title),
                                      cat_selected=c.pk)
        c_def['menu'] = menu
        return dict(list(context.items()) + list(c_def.items()))


class AddProjectView(CreateView):
    model = Project
    form_class = ProjectForm
    template_name = "webpage/add.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        return context


class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'webpage/project_update.html'
    template_name_suffix = '_update'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        return context


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
