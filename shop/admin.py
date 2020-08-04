from django.contrib import admin
from django.utils.safestring import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from .models import Category, Product, Reviews

from import_export.admin import ImportExportActionModelAdmin
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget


class ProductAdminForm(forms.ModelForm):
    characteristics = forms.CharField(label="Характеристики", widget=CKEditorUploadingWidget())

    class Meta:
        model = Product
        fields = '__all__'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


class ProductResource(resources.ModelResource):

    class Meta:
        model = Product


@admin.register(Product)
class ProductAdmin(ImportExportActionModelAdmin):
    resource_class = ProductResource
    list_display = ['name', 'price', 'stock', 'created','get_image']
    list_filter = ['created']
    list_editable = ['price', 'stock']
    prepopulated_fields = {'slug': ('name',)}
    form = ProductAdminForm
    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')



@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    readonly_fields = ('name', 'lastname')
