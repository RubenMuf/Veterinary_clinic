from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models
from clinic.models import Pet, Onwer

class SignUpform(UserCreationForm): # форма для регистрауии как пользователя системы
    login_username = forms.CharField(label="Логин", help_text='',
                               widget=forms.TextInput(attrs={'placeholder': 'Багира'}))
    password1 = forms.CharField(label='Пароль', help_text='',
                                widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}))
    password2 = forms.CharField(label='Подтверждение', help_text='',
                                widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}))
    email = forms.EmailField(label='Почта',
                             widget=forms.TextInput(attrs={'placeholder': 'bagira@mail.ru'}))

    # '''
    # старый метод
    # username = forms.CharField(label="Логин", help_text='',
    #                            widget=forms.TextInput(attrs={'placeholder': 'Багира'}))
    # password1 = forms.CharField(label= 'Пароль', help_text='', widget=forms.PasswordInput(attrs={'autocomplete':'new-password'}))
    # password2 = forms.CharField(label='Подтверждение', help_text='', widget=forms.PasswordInput(attrs={'autocomplete':'new-password'}))
    #
    # view = forms.CharField(label='Вид', max_length=15, min_length=2,
    #                         error_messages={
    #                             'required': 'Напишите вид'
    #                         },
    #                        widget=forms.TextInput(attrs={'placeholder': 'Кошка'}))
    #
    # breed = forms.CharField(label='Порода', max_length=15,
    #                          error_messages={
    #                              'required': 'Напишите породу'
    #                          },
    #                         widget=forms.TextInput(attrs={'placeholder': 'Сиамская'}))
    #
    # nick_name = forms.CharField(label='Кличка', max_length=15,
    #                              error_messages={
    #                                  'required': 'Напишите кличку'
    #                              },
    #                             widget=forms.TextInput(attrs={'placeholder': 'Багира'}))
    # age = forms.DecimalField(label='Возраст', min_value=1)
    # weight = forms.DecimalField(label='Вес', min_value=1)
    # list_gender = (('Самец', 'Самец'), ('Самка', 'Самка'))
    # gender = forms.TypedChoiceField(label='Пол', choices=list_gender)
    # firstname_onwer = forms.CharField(label='Имя хозяина',
    #                                   widget=forms.TextInput(attrs={'placeholder': 'Иван'}))
    # lastname_onwer = forms.CharField(label='Фамилия хозяина',
    #                                  widget=forms.TextInput(attrs={'placeholder': 'Иванов'}))
    # email_onwer = forms.CharField(label='E-mail хозяина',
    #                               widget=forms.TextInput(attrs={'placeholder': 'olenevod@mail.ru'}))
    # tel_onwer = forms.CharField(label='Телефон хозяина',
    #                             widget=forms.TextInput(attrs={'placeholder': '+79030001122'}))
    # # img_ = forms.ImageField(label='Выберите файл')
    # '''

class Edit_a_profile(forms.ModelForm): # создаем форму на основе модели Питомца
    onwer = forms.ModelChoiceField(queryset=Onwer.objects.all(), required=False,
                                   empty_label='Нет хозяина', label='Хозяин:')
    class Meta:
        model = Pet
        fields = ['view', 'breed', 'photo', 'nick_name', 'age', 'weight']











