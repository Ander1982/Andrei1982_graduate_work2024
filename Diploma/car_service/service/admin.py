from django.contrib import admin
from .models import Service, Order, StatusOrder, Staff, Review, Rec
from django.utils.safestring import mark_safe


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'get_img',)
    fields = ('title', 'description', 'image', 'get_img')
    readonly_fields = ('get_img',)

    def get_img(self, obj):
        if obj.image:
            return mark_safe(f"<img src='{obj.image.url}' width='80'>")

    get_img.short_description = 'Миниатюра'


class RecAdmin(admin.ModelAdmin):
    list_display = ('rec_name', 'rec_day', 'rec_time')
    fields = ('rec_name', 'rec_day', 'rec_time')


class StaffAdmin(admin.ModelAdmin):
    list_display = ('name', 'categories', 'skills', 'vote_total', 'vote_ratio', 'get_img',)
    readonly_fields = ('get_img',)

    def get_img(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' width='80'>")

    get_img.short_description = 'Миниатюра'


admin.site.register(Service, ServiceAdmin)
admin.site.register(StatusOrder)
admin.site.register(Order)
admin.site.register(Staff, StaffAdmin)

admin.site.register(Review)
admin.site.register(Rec, RecAdmin)
