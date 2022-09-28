from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView
from .forms import AddProjectForm
from .models import *
from .utils import DataMixin

# menu settings
menu = [{'text': 'Изменить', 'url': '/admin/webpage/project/'}, ]
cats = Category.objects.all()
for c in cats:
    menu.append({'text': c.title, 'url': f'/category/{c.slug}'})


# menu settings

def index(request):
    return redirect('category/stroitelno-montazhnye-raboty')


class add(CreateView):
    template_name = 'webpage/add.html'
    success_url = '/'
    form_class = AddProjectForm


class ProjectCategory(DataMixin, ListView):
    model = Project
    template_name = 'webpage/index.html'
    context_object_name = 'projects'
    active_manager = None
    active_company = None

    def get_queryset(self):
        if(self.request.GET):
            if (self.request.GET['manager']):
                managers = self.request.GET['manager'].split(',')
                self.active_manager = Manager.objects.filter(id__in=managers)
            if (self.request.GET['company']):
                companies = self.request.GET['company'].split(',')
                self.active_company = Company.objects.filter(id__in=companies)
            return Project.objects.filter(cat__slug=self.kwargs['cat_slug'], manager__pk__in=managers, company__pk__in=companies).select_related('cat')
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
        c = Category.objects.get(slug=self.kwargs['cat_slug'])
        context['category'] = c
        c_def = self.get_user_context(title='Category - ' + str(c.title),
                                      cat_selected=c.pk)
        return dict(list(context.items()) + list(c_def.items()))
