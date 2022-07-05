from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse


# Приявязка профиля к созданной модели пользователя


class Profile(models.Model):
    """
    Поля профиля: пользователь (к которому привязан профиль),
    имя, о себе, локация, дата рождения, аватарка.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    name = models.CharField(max_length=50, blank=True, null=True, verbose_name='Имя')
    bio = models.TextField(max_length=500, blank=True, verbose_name='О себе')
    location = models.CharField(max_length=30, blank=True, verbose_name='Локация')
    birth_date = models.DateField(null=True, blank=True, verbose_name='Дата рождения')
    avatar = models.ImageField(upload_to='profiles/avatars', blank=True, null=True, verbose_name='Аватар')

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        """  Ссылка на просмотр профиля  """
        return reverse('accounts:profile', kwargs={'pk': self.pk})


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Сигнал для создания и привязки профиля
    к пользователю при создании пользователя
    """
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """  Сигнал для сохранения  """
    instance.profile.save()
