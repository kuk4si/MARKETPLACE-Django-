from django.contrib import admin
from .models import *


# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    class Meta:
        model = Product

    list_display = ('name', 'price',)
    search_fields = ['name', 'description']


admin.site.register(Product, ProductAdmin)
