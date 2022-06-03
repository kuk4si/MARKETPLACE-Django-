from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView

from .models import Product
from .forms import ProductForm


def home(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products/home.html', context)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/detail.html'


def create(request):
    user = request.user
    form = ProductForm(initial={'owner': user})
    if request.method == 'POST':
        data = request.POST
        if data:
            owner = user
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'products/add_product.html', {'form': form})


# class ProductCreateView(CreateView):
#     model = Product
#     form_class = ProductForm
#     template_name = 'products/add_product.html'
#     success_url = reverse_lazy('products:home')
