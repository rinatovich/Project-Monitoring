from django.conf.urls.static import static
from django.urls import path

from PMS import settings
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('construction', index, name='construction'),
    path('projects', index, name='projects'),
    path('add', add.as_view(), name='add'),
    path('techservice', index, name='techservice'),
    path('category/<slug:cat_slug>/', ProjectCategory.as_view(), name='category')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)