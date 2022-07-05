from django.contrib import admin
from .models import Profile


class AdminProfile(admin.ModelAdmin):
    class Meta:
        model = Profile

    list_display = ('user', 'name',)
    search_fields = ['name']


admin.site.register(Profile, AdminProfile)
