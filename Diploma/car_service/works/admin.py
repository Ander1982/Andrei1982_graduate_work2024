from django.contrib import admin, messages
from .models import Works, ProductCategory, Product, Photo
from django.utils.safestring import mark_safe
from django.urls import path
from django.shortcuts import render, redirect
from django import forms


class CsvImportForm(forms.Form):
    csv_uploader = forms.FileField()


class WorksAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'date')


class PhotoAdd(admin.StackedInline):
    model = Photo
    fields = ("product", "add_photo")
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price', 'quantity')
    list_display_links = ('id', 'name')
    inlines = [PhotoAdd]

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path("upload-product-csv/", self.upload_csv)]
        return new_urls + urls

    def upload_csv(self, request):
        if request.method == "POST":
            csv_file = request.FILES['csv_uploader']

            if not csv_file.name.endswith('.csv'):
                messages.warning(request, "Ошибочный тип файла")
                return redirect('.')

            file_data = csv_file.read().decode("utf-8")
            csv_data = file_data.split("\n")

            for x in csv_data:
                fields = x.split(",")
                created = Product.objects.update_or_create(
                    id=fields[0],
                    name=fields[1],
                    image=fields[2],
                    description=fields[3],
                    short_description=fields[4],
                    price=fields[5],
                    quantity=fields[6][:-1],
                    category=ProductCategory(fields[7][0]),
                )

            return redirect('admin:index')

        form = CsvImportForm()
        data = {"form": form}
        return render(request, "admin/csv_uploader.html", data)


class PhotoAdmin(admin.ModelAdmin):
    list_display = ("product", "add_photo")

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path("upload-photo-csv/", self.upload_csv)]
        return new_urls + urls

    def upload_csv(self, request):
        if request.method == "POST":
            csv_file = request.FILES['csv_uploader']

            if not csv_file.name.endswith('.csv'):
                messages.warning(request, "Ошибочный тип файла")
                return redirect('.')

            file_data = csv_file.read().decode("utf-8")
            csv_data = file_data.split("\n")

            for x in csv_data:
                fields = x.split(",")
                created = Photo.objects.update_or_create(
                    id=fields[0],
                    product=Product(fields[1]),
                    add_photo=fields[2][:-1],
                )

            return redirect('admin:index')

        form = CsvImportForm()
        data = {"form": form}
        return render(request, "admin/csv_uploader.html", data)


class ProductCategoryAdmin(admin.ModelAdmin):
    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path("upload-csv/", self.upload_csv)]
        return new_urls + urls

    def upload_csv(self, request):
        if request.method == "POST":
            csv_file = request.FILES['csv_uploader']

            if not csv_file.name.endswith('.csv'):
                messages.warning(request, "Ошибочный тип файла")
                return redirect('.')

            file_data = csv_file.read().decode("utf-8")
            csv_data = file_data.split("\n")

            for x in csv_data:
                fields = x.split(",")
                created = ProductCategory.objects.update_or_create(
                    id=fields[0],
                    name=fields[1],
                    description=fields[2],
                )

            return redirect('admin:index')

        form = CsvImportForm()
        data = {"form": form}
        return render(request, "admin/csv_uploader.html", data)


admin.site.register(Works, WorksAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)

# Register your models here.
