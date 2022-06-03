from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('<slug:slug>/', ProductDetailView.as_view(), name='detail'),
    path('products/add/', create, name='add'),
]
