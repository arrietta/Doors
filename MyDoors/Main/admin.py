from django.contrib import admin
from .models import Door


class DoorAdmin(admin.ModelAdmin):
    list_display = ('collection', 'shape', 'portal', 'bevel', 'molding', 'color', 'price',)
    list_filter = ('collection', 'shape', 'portal', 'bevel', 'molding', 'color', 'price')


admin.site.register(Door, DoorAdmin)
