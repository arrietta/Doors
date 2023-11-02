from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('main', views.main, name='main'),
    path('', views.catalog, name='catalog'),
    path('basket/', views.basket, name='basket'),
    path('Delete/<int:pk>/', views.delete, name='delete'),
    path('save/', views.save, name='save'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
