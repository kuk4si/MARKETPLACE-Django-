from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.hashers import check_password
from django.forms import ValidationError
from .models import Profile
from django.forms.widgets import ClearableFileInput


class MyClearableFileInput(ClearableFileInput):
    initial_text = ''
    input_text = 'Изменить'
    clear_checkbox_label = 'clear'


User = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'username'
    }))

    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'password'
    }))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            qs = User.objects.filter(username=username)
            if not qs.exists():
                raise ValidationError('Такого пользователя нет')
            if not check_password(password, qs[0].password):
                raise ValidationError('Неверный пароль')
            user = authenticate(username=username, password=password)
            if not user:
                raise ValidationError('Данный пользователь не активен')
        return super().clean(*args, **kwargs)


class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username'
    }))

    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password'
    }))

    password2 = forms.CharField(label='Пароль опять', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password again'
    }))

    class Meta:
        model = User
        fields = ('username',)

    def clean_password2(self):
        data = self.cleaned_data
        if data['password'] != data['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return data['password']


class ProfileEditForm(forms.ModelForm):
    name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={
        'class': 'form-control name_field col-5',
        'placeholder': ''
    }))

    bio = forms.CharField(label='О себе', widget=forms.Textarea(attrs={
        'class': 'form-control bio_field col-5',
        'placeholder': '',
    }))

    avatar = forms.ImageField(label='Текущий аватар', widget=MyClearableFileInput)

    class Meta:
        model = Profile
        fields = ('name', 'bio', 'avatar',)
