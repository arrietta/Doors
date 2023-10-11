from django.contrib import admin
from .models import Shape, Molding, Portal, Color, Door, Bevel


class ShapeAdmin(admin.ModelAdmin):
    list_display = ('name',)


class PortalAdmin(admin.ModelAdmin):
    list_display = ('name', 'shape',)
    list_filter = ('molding__shape',)


class BevelAdmin(admin.ModelAdmin):
    list_display = ('name', 'shape', 'portal',)
    list_filter = ('shape',)


class MoldingAdmin(admin.ModelAdmin):
    list_display = ('name', 'shape', 'portal', 'bevel')
    list_filter = ('shape',)


class ColorAdmin(admin.ModelAdmin):
    list_display = ('name',)


class DoorAdmin(admin.ModelAdmin):
    list_display = ('shape', 'portal', 'bevel', 'molding', 'color', 'price',)
    list_filter = ('shape', 'portal', 'bevel', 'molding', 'color', 'price')


admin.site.register(Shape, ShapeAdmin)
admin.site.register(Portal, PortalAdmin)
admin.site.register(Bevel, BevelAdmin)
admin.site.register(Molding, MoldingAdmin)
admin.site.register(Color, ColorAdmin)
admin.site.register(Door, DoorAdmin)
