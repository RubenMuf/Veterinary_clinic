from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView, UpdateView
from django.core.paginator import Paginator
from .models import *
from django.views import generic # для списков питомцев и других объектов

from clinic.models import Veterinarian, Pet
from .forms import SignUpform, Edit_a_profile
from clinic import mybibl
from clinic.utils import *

# Create your views here.

#tgbvfredc741

# def index(request):
#     if request.user.username:
#         user_first_name = request.user.username
#
#     else:
#         user_first_name = 'Гость'
#         print('Гость и у него соответственно нет аватара')
#
#     data = {'user_first_name': user_first_name}
#     return render(request, 'clinic/index.html', context=data)

class PetHome(DataMixin, ListView): # главная страница. DataMixin - наполнение шаблонов стандартной информацией - записывают его первым
    template_name = 'clinic/index.html'
    # context_object_name =
    title_page = 'Главная страница' # название в пути, формируется в классе DataMixin
# def veterinarian(request):
#     # vet_list = Veterinarian.objects.all()  # старая версия вывода на экран
#     # data = {'vet_list': vet_list}
#     return render(request, 'clinic/veterinarian_list.html')

    def get_queryset(self): # формирует параметр для пути, открывать выбранную позицию
        return Pet.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        user_first_name = user.username if user.is_authenticated else 'Гость'
        context['user_first_name'] = f'Привет, {user_first_name}!'
        context['avatar'] = 'clinic/img/logo_link/no_avatar.png' if not user.is_authenticated else 'clinic/img/logo_link/admin.png'
        return context

class Pet_list(LoginRequiredMixin, DataMixin, ListView): # модель на классе на модели метод весь список LoginRequiredMixin - класс для закрытия от неавторизованных пользователей, отправляет на страницу со входом в систему, а после переводит на страницу на которую пользователь хотел попасть.
    model = Pet
    template_name = 'clinic/pet_list.html'
    title_page = 'Список наших пациентов' # название в пути, формируется в классе DataMixin
    login_url = '/admin/' # путь для перевода на определенную страницу неавторизованного пользователя
    # paginate_by = 3 # джанговская функция по сколько питомцев выводить на страницу, работает в связке с остальным кодом на файле HTML
class Pet_detail(DataMixin, DetailView): # модель на классе на модели метод один объект из списка
    model = Pet
    title_page = 'Подробно о питомце' # название в пути, формируется в классе DataMixin

class Veterinarian_list(DataMixin, ListView): # модель на классе на модели метод весь список
    model = Veterinarian
    title_page = 'Список ветеринаров'  # название в пути, формируется в классе DataMixin

    # paginate_by = 3 # джанговская функция по сколько фильмов выводить на страницу, работает в связке с остальным кодом на файле HTML
class Veterinarian_detail(DataMixin, DetailView): # модель на классе на модели метод один объект из списка
    model = Veterinarian
    title_page = 'Подробно о ветеринаре'  # название в пути, формируется в классе DataMixin

def record(request): # фунция вывода всех записей к врачу, пока временно
    record = Record.objects.all()
    data = {'record': record}
    return render(request, 'clinic/record.html', data)

from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login
def registration(request): # регистрация/авторизация только пользователя в джанговскую таблицу user, дальше уже зарегистрированный в общей базе пользователь сам на свое усмотрение заполняет свои данные
    print(1)
    if request.method == 'POST': # первая проверка на экране
        print(2)
        form = SignUpform(request.POST) # присваеваем в переменную на форму которая в файле shape на классе
        if form.is_valid():  # вторая проверка которая на сервере
            print(3)
            form.save() # сохраняет как html страницу так как работаем по готовому джанговскому методу
            print(form.cleaned_data)
            try:
                # User.objects.create(**form.cleaned_data) # метод который сам вытаскивает запроса данные для сохранения в бд
                login_username = form.cleaned_data.get('login_username')
                password = form.cleaned_data.get('password1')
                email = form.cleaned_data.get('email')
                user = authenticate(username=login_username, password=password)  # сохраняет нового пользователя
                man = User.objects.get(username=login_username)  # найдем нового только что созданного в таблице user юзера
                # заполним поля в таблице user, которая используется для админа
                man.first_name = login_username
                man.email = email
                man.save()
                login(request, user) # вход в пользователя в систему
                return redirect('home')
            except:
                form.add_error(None, 'Ошибка добавления пользователя') # если выскакивает ошибка

            return redirect('home') # если форма полностью правильна заполнена - то выходим на главную страницу
    else:
        form = SignUpform() # если форма не заполнена - то загружает страницу по новой
    data={'form': form}
    return render(request,'registration/registration.html', context=data)

class AddEdit_a_profile(CreateView): # класс представления для вывода формы
    # form_class = Edit_a_profile # создаем форму, но не вызываем, а прописываем только ссылку на класс без ()
    model = Pet
    fields = '__all__'
    template_name = 'edit_a_profile/edit_a_profile.html'
    # success_url = reverse_lazy('home')# это формирует путь после того как форма у пользователя будет успешно и правильно заполнена и только в момент когда это путь действительно нужен  # это тоже не нужно так как все построено на модели и само откроет ListDeteil

    # extra_context = {  # данные, которые выгружаем на шаблон, в данном случае только статические - которые нам известны
    #     'menu': menu,
    #     'title': 'Добавление статьи',
    # }
    # def form_valid(self, form): # метод на проверку валидности формы которую заполнил юзер теперь это не нужно так так класс на модели CreateView сам проверяет валидность
    #     form.save() # сохранение данных в таблицу
    #     return super().form_valid(form)

def page_not_found(request, exception): # настройка если страница не найдена продолжение в urls основной, второй параметр обязателен
    return HttpResponseNotFound('<h1>Страница не найдена!</h1>')
















# def index(request):
#     if request.user.username:
#         user_first_name = request.user.first_name
#         img = 'clinic/img/logo_link/no_avatar.png'
#         # print(user_first_name)
#         # user_l_name = request.user.last_name
#         if user_first_name == 'Главный':
#             img = 'clinic/img/logo_link/admin.png'
#             if Pet.objects.filter(nick_name=user_first_name and Pet.objects.filter(nick_name=user_first_name).image):
#                 print('***')
#                 # if Pet.objects.get(nick_name=user_first_name).image: # если в таблице питомца есть путь в поле image
#                 img = Pet.objects.get(nick_name=user_first_name).image # то присваеваем ему его аватар
#                 print('Питомец с аватаром', img)
#     else:
#         user_first_name = 'Гость'
#         # user_l_name = '*****'
#         # img = 'clinic/img/logo_link/no_avatar.png'
#         print('Гость и у него соответственно нет аватара')
#
#     data = {'user_first_name': user_first_name, 'img': img}
#
#     return render(request, 'clinic/index.html', context=data)






