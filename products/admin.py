from django.contrib import admin
from .models import *


class ProductAdmin(admin.ModelAdmin):
    class Meta:
        model = Product

    list_display = ('name', 'price', 'owner', 'is_published')
    search_fields = ['name', 'description']


admin.site.register(Product, ProductAdmin)
