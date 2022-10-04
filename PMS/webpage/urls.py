from django.conf.urls.static import static
from django.urls import path

from PMS import settings
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('category/<slug:cat_slug>/', ProjectCategory.as_view(), name='category'),
    path('project/update/<slug:slug>/', UpdateProject.as_view(), name='update_project'),
    path('project/add', AddProject.as_view(), name='add'),
    path('project/<slug:slug>', ShowProject.as_view(), name='project'),
    path('login', LoginUser.as_view(), name='login'),
    path('logout', logout_user, name='logout')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
