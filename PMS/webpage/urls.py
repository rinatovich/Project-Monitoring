from django.conf.urls.static import static
from django.urls import path

from PMS import settings
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('category/<slug:cat_slug>/', ProjectCategory.as_view(), name='category'),
    path('project/<slug:slug>/', ProjectUpdateView.as_view(), name='project'),
    path('project/add', AddProjectView.as_view(), name='add')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
