from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView
from .forms import ProjectForm, LoginUserForm
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


class ProjectCategory(LoginRequiredMixin, DataMixin, ListView):
    login_url = '/login'
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
            elif 'customer' in self.request.GET:
                customers = self.request.GET['manager'].split(',')
                self.active_customer = Project.objects.filter(customer=customers)[0].customer
                return Project.objects.filter(cat__slug=self.kwargs['cat_slug'],
                                              customer=customers).select_related('cat')
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


class AddProject(CreateView, LoginRequiredMixin):
    login_url = '/login'
    model = Project
    form_class = ProjectForm
    template_name = "webpage/add.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        return context


class UpdateProject(UpdateView, LoginRequiredMixin):
    login_url = '/login'
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


class ShowProject(DetailView, LoginRequiredMixin):
    login_url = '/login'
    model = Project
    template_name = 'webpage/project.html'

    def post(self, request, *args, **kwargs):
        try:
            checboxes = dict(request.POST)["checkbox"]
            for c in checboxes:
                Note.objects.filter(pk=c).delete()
            return HttpResponseRedirect(self.request.path_info)
        except:
            project = Project.objects.filter(slug=kwargs['slug'])[0]
            note = Note.objects.create(user=request.user, text=request.POST['text'])
            project.note.add(note)
            return HttpResponseRedirect(self.request.path_info)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        return context


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'webpage/login.html'

    def get_success_url(self):
        return reverse_lazy('index')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        return context


def logout_user(request):
    logout(request)
    return redirect('login')
