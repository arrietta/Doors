from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('api/moldings/', views.get_moldings_by_shape, name='get_moldings_by_shape'),
    path('api/portals/', views.get_portals_by_molding, name='get_portals_by_molding'),
    path('api/colors/', views.get_colors_by_portal, name='get_colors_by_portal'),

]
