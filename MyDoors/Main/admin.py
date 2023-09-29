from django.contrib import admin
from .models import Shape, Molding, Portal, Color, Door

class ShapeAdmin(admin.ModelAdmin):
    list_display = ('name',)

class MoldingAdmin(admin.ModelAdmin):
    list_display = ('name', 'shape',)
    list_filter = ('shape',)

class PortalAdmin(admin.ModelAdmin):
    list_display = ('name', 'molding', 'shape',)
    list_filter = ('molding__shape',)

class ColorAdmin(admin.ModelAdmin):
    list_display = ('name',)

class DoorAdmin(admin.ModelAdmin):
    list_display = ('shape', 'molding', 'portal', 'color', 'price',)
    list_filter = ('shape', 'molding', 'portal', 'color',)

admin.site.register(Shape, ShapeAdmin)
admin.site.register(Molding, MoldingAdmin)
admin.site.register(Portal, PortalAdmin)
admin.site.register(Color, ColorAdmin)
admin.site.register(Door, DoorAdmin)
