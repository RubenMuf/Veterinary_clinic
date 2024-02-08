import datetime

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm

from clinic.models import Pet, Onwer


class LoginUsersForm(AuthenticationForm): # наследуем от готового решения класса джанго
    username = forms.CharField(label='Логин',
                               widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = get_user_model() # готовая функция джанго
        # fields = ['password', 'username']

class RegisterUserForm(UserCreationForm): #авторизация, так как форма связана с моделью - вложенный класс
    username = forms.CharField(label='Логин',
                               widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput({'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля',
                               widget=forms.PasswordInput({'class': 'form-input'}))

    class Meta:
        model = get_user_model() # значения модели вернем с помощьюю метода get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        labels = {
            'email': 'E-mail',
            'first_name': 'Имя',
            'last_name': 'Фамилия'
        }

        widgets = { # стили как будет выглядеть форма
            'email': forms.TextInput(attrs={'class': 'form-input'}),
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input'}),
        }

    # def clean_password2(self): # валидатор на проверку паролей # это нужно было для функции представления, но теперь у нас класс представления и джанго класс UserCreationForm берет это все на себя.
    #     cd = self.cleaned_data # присваиваем инфу в переменную
    #     if cd['password'] != cd['password2']: # сравниваем пароли
    #         raise forms.ValidationError('Пароли не совпадают!') # если не совпадают то выдаем на страницу ошибку
    #     return cd['password'] # если все норм то возвращаем


    def clean_email(self): # валидатор на проверку уникальности E-mail
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError('Такой E-mail уже существует!')
        return email

class ProfileUserForm(forms.ModelForm): #редактирование собственного профиля на моделе, так как связано с моделью, для создания профиля пользователя
    username = forms.CharField(disabled=True, label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'})) # disabled - (отключеный), чтобы невозможно было изменять параметр
    email = forms.CharField(disabled=True, label='E-mail', widget=forms.TextInput(attrs={'class': 'form-input'}))
    this_year = datetime.date.today().year
    data_birth = forms.DateField(widget=forms.SelectDateWidget(years=tuple(range(this_year - 100, this_year - 5))))
    class Meta:
        model = get_user_model() # связываем с текущей моделью
        fields = ['username', 'email',  'photo', 'data_birth',  'first_name', 'last_name'] # поля отображения
        labels = { # названия полей
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'photo': 'Аватар',
            'data_birth': 'Дата рождения',
        }
        widgets = { # настройки полей
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input'}),
        }

class UserPasswordChangeForm(PasswordChangeForm): # для отображения изменения пароля пользователя
    old_password = forms.CharField(label='Старый пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    new_password1 = forms.CharField(label='Новый пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    new_password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

# class Edit_a_profile(forms.ModelForm): # создаем форму на основе модели Питомца перенес из папки клиника
#     onwer = forms.ModelChoiceField(queryset=Onwer.objects.all(), required=False,
#                                    empty_label='Нет хозяина', label='Хозяин:')
#     class Meta:
#         model = Pet
#         fields = ['view', 'breed', 'photo', 'nick_name', 'age', 'weight']