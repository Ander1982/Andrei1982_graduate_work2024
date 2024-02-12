from django.contrib import admin
from .models import Service
from django.utils.safestring import mark_safe


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'get_img')
    fields = ('title', 'description', 'image', 'get_img')
    readonly_fields = ('get_img',)

    def get_img(self, obj):
        if obj.image:
            return mark_safe(f"<img src='{obj.image.url}' width='80'>")

    get_img.short_description = 'Миниатюра'


admin.site.register(Service, ServiceAdmin)
