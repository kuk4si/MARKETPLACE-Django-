from django import forms
from django.contrib.auth.models import User

from .models import Product


# Configure form
class ProductForm(forms.ModelForm):

    owner = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.HiddenInput())

    name = forms.CharField(label='Наименование', widget=forms.TextInput(attrs={
        'class': 'form-control',  # <input class="form-control">
        'placeholder': 'Введите название'
    }))

    price = forms.DecimalField(label='Цена', widget=forms.NumberInput(attrs={
        'class': 'form-control',  # <input class="form-control">
        'placeholder': 'Укажите цену (в рублях)'
    }))

    description = forms.CharField(label='Описание', widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Описание товара'
    }))

    class Meta:
        model = Product
        # fields = ('name', 'price', 'description',)
        fields = '__all__'



