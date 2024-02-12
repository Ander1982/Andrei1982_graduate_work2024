from django.contrib import admin
from .models import Works
from django.utils.safestring import mark_safe


class WorksAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'date')


admin.site.register(Works, WorksAdmin)

# Register your models here.
