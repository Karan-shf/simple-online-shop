from django.contrib import admin
from . import models

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ['slug']
    list_display = ['title','price','rating','numbers','sale_count']
    list_editable = ['price','rating','sale_count']

admin.site.register(models.Product,ProductAdmin)
admin.site.register(models.Category)