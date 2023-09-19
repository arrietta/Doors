# doors/admin.py

from django.contrib import admin
from .models import Shape, Color, Molding, Portal, Door

admin.register(Door)


@admin.register(Shape)
class AttributeAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Color)
class AttributeAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Molding)
class AttributeAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Portal)
class AttributeAdmin(admin.ModelAdmin):
    list_display = ['name']
