from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView

from .models import Product


def home(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products/home.html', context)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/detail.html'
