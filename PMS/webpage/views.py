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

    def get_queryset(self):
        if(self.request.GET):
            managers = self.request.GET['manager'].split(',')
            return Project.objects.filter(cat__slug=self.kwargs['cat_slug'], manager__pk__in=managers).select_related('cat')
        else:
            return Project.objects.filter(cat__slug=self.kwargs['cat_slug']).select_related('cat')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['iter'] = 1
        c = Category.objects.get(slug=self.kwargs['cat_slug'])
        context['category'] = c
        c_def = self.get_user_context(title='Category - ' + str(c.title),
                                      cat_selected=c.pk)
        return dict(list(context.items()) + list(c_def.items()))
