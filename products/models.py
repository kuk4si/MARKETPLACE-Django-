from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


from django.template.defaultfilters import slugify as django_slugify

alphabet = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i',
            'й': 'j', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
            'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ы': 'i', 'э': 'e', 'ю': 'yu',
            'я': 'ya'}


def slugify(s):
    """
    Overriding django slugify that allows to use russian words as well.
    """
    return django_slugify(''.join(alphabet.get(w, w) for w in s.lower()))


class Product(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products', verbose_name='Владелец')
    name = models.CharField(max_length=100, verbose_name='Название')
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Цена')
    description = models.TextField(verbose_name='Описание')
    slug = models.SlugField(max_length=255, unique=True, default='auto', verbose_name='Slug')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Время публикации')
    is_published = models.BooleanField(default=False, verbose_name='Статус')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)