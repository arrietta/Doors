from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('basket/', views.basket, name='basket'),
    path('Delete/<int:pk>/', views.delete, name='delete'),
    path('save/', views.save, name='save'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
