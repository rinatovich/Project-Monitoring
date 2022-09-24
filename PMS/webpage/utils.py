from django.core.cache import cache
from django.db.models import Count

from .models import *

menu = [{'text': 'Изменить', 'url': '/admin/webpage/project/'},]
cats = Category.objects.all()
for c in cats:
    menu.append({'text': c.title, 'url': f'/category/{c.slug}'})


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = cache.get('cats')
        if not cats:
            cats = Category.objects.annotate(Count('project'))
            cache.set('cats', cats, 60)

        context['cats'] = cats
        context['menu'] = menu

        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context
