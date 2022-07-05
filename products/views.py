from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView

from .models import Product
from .forms import ProductForm


def home(request):
    """  Начальная страница просмотра товаров, домашняя страница"""
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products/home.html', context)


class ProductDetailView(DetailView):
    """  Просмотр выбраного товара  """
    model = Product
    template_name = 'products/detail.html'


class ProductUpdateView(UpdateView):
    """  Редактирование товара  """
    model = Product
    template_name = 'products/update.html'
    form_class = ProductForm


def create(request):
    """
    Создание товара пользователем, если пользователь
    не вошел в сиистему, его перебросит на страницу регистрации.
    Форма автоматически генерирует скрытое поле пользователя.
    """
    user = request.user
    if request.user.is_anonymous:
        return redirect('/accounts/register')
    form = ProductForm(initial={'owner': user})
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('/')
    return render(request, 'products/add_product.html', {'form': form})
