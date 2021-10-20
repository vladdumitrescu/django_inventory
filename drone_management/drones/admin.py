from django.contrib import admin

# Register your models here.

from .models import Drone, CameraBrand


class DroneAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'brand', 'price', 'is_published', 'created_at')
    list_display_links = ('id', 'name')
    list_filter = ('name', 'brand', 'camera_megapixel', 'price')
    list_editable = ('is_published',)
    search_fields = ('name', 'brand', 'camera_model', 'camera_megapixel', 'camera_brand', 'price')
    ordering = ('price',)
    # exclude = ('description',)


admin.site.register(Drone, DroneAdmin)
admin.site.register(CameraBrand)
