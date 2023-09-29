from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('api/moldings/', views.get_moldings_by_shape, name='get_moldings_by_shape'),
    path('api/portals/', views.get_portals_by_molding, name='get_portals_by_molding'),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)