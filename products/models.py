from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Цена')
    description = models.TextField(verbose_name='Описание')
    slug = models.SlugField(max_length=255, unique=True, default='auto', verbose_name='Slug')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Время публикации')
    is_published = models.BooleanField(default=False, verbose_name='Статус')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)