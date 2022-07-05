from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.generic import UpdateView
from .models import Profile
from .forms import UserLoginForm, UserRegistrationForm
from .forms import ProfileEditForm


def login_view(request):
    """  Форма входа  """
    form = UserLoginForm(request.POST or None)
    _next = request.GET.get('next')
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        _next = _next or '/'
        return redirect(_next)
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    """  Выход из аккаунта  """
    logout(request)
    return redirect('/')


def registration_view(request):
    """  Регистрация  """
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])  # Правильная шифровка пароля
            new_user.save()
            return render(request, 'accounts/register_done.html', {'new_user': new_user})
        return render(request, 'accounts/register.html', {'form': form})
    else:
        form = UserRegistrationForm()
        return render(request, 'accounts/register.html', {'form': form})


def profile(request, pk):
    """  Просмотр профиля  """
    if request.user.is_authenticated:
        user = User.objects.get(pk=pk)
        qs = user.products.all()
        context = {'user': user, 'qs': qs}
        return render(request, 'accounts/profile.html', context)
    else:
        return redirect('/accounts/register')


class ProfileUpdate(UpdateView):
    """  Редактирование профиля"""
    model = Profile
    form_class = ProfileEditForm
    template_name = 'accounts/profile_update.html'


"""
    ДОПОЛНЕНИЕ:
Некотарая логика прописана в HTML файлах, такая как,
проверка текущего пользователя на возможность редактировать профиль,
что бы другой пользователь не смог отредактировать чужой профиль. Редактирование
товаров.
"""
