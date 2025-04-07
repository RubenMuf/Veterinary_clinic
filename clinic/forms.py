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



class Edit_a_profile(forms.ModelForm): # создаем форму на основе модели Питомца
    onwer = forms.ModelChoiceField(queryset=Onwer.objects.all(), required=False,
                                   empty_label='Нет хозяина', label='Хозяин:')
    class Meta:
        model = Pet
        fields = ['view', 'breed', 'photo', 'nick_name', 'age', 'weight']

from .models import Comment
class CommentCreateForm(forms.ModelForm):
    """
    Форма добавления комментариев к статьям
    """
    parent = forms.IntegerField(widget=forms.HiddenInput, required=False)
    content = forms.CharField(label='', widget=forms.Textarea(attrs={'cols': 30, 'rows': 5, 'placeholder': 'Комментарий', 'class': 'form-control'}))

    class Meta:
        model = Comment
        fields = ('content',)










