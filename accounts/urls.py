from django.urls import path
from .views import *

urlpatterns = [
    path('logout', logout_view, name='logout'),
    path('login', login, name='login'),
    path('register', register, name='register'),
]
