from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404, JsonResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView, UpdateView
from django.core.paginator import Paginator

from Veterinary_clinic import settings
from .models import *
from django.views import generic # для списков питомцев и других объектов

from clinic.models import Veterinarian, Pet
from .forms import SignUpform, Edit_a_profile
from clinic import mybibl
from clinic.utils import *

from .forms import CommentCreateForm
from .models import Comment

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
    title_page = 'Главная страница' # название в пути, формируется в классе DataMixin

    def get_queryset(self): # формирует параметр для пути, открывать выбранную позицию
        return Pet.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        user_first_name = user.username if user.is_authenticated else 'Гость'
        context['user_first_name'] = f'Привет, {user_first_name}!'
        context['avatar'] = settings.DEFAULT_USER_IMAGE # берем путь из функции в сетинге, чтобы если вдруг что-то поменяется, фото всегда было доступно
        # context['avatar'] = 'clinic/img/logo_link/no_avatar.png' if not user.is_authenticated else 'clinic/img/logo_link/no_avatar.png'
        return context

class Pet_list(LoginRequiredMixin, DataMixin, ListView): # модель на классе на модели метод весь список LoginRequiredMixin - класс для закрытия от неавторизованных пользователей, отправляет на страницу со входом в систему, а после переводит на страницу на которую пользователь хотел попасть.
    model = Pet
    template_name = 'clinic/pet_list.html'
    title_page = 'Список наших пациентов' # название в пути, формируется в классе DataMixin
    login_url = 'users:login' # путь для перевода на страницу авторизации(входа в систему) неавторизованного пользователя
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


class AddEdit_a_profile(CreateView): # форма добавление питомца в БД класс представления для вывода формы
    model = Pet
    fields = '__all__'
    template_name = 'edit_a_profile/edit_a_profile.html'



def services(request):
    return render(request, 'clinic/services.html')

def page_not_found(request, exception): # настройка если страница не найдена продолжение в urls основной, второй параметр обязателен
    return HttpResponseNotFound('<h1>Страница не найдена!</h1>')

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentCreateForm

    def is_ajax(self):
        return self.request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    def form_invalid(self, form):
        if self.is_ajax():
            return JsonResponse({'error': form.errors}, status=400)
        return super().form_invalid(form)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.article_id = self.kwargs.get('pk')
        comment.author = self.request.user
        comment.parent_id = form.cleaned_data.get('parent')
        comment.save()

        if self.is_ajax():
            return JsonResponse({
                'is_child': comment.is_child_node(),
                'id': comment.id,
                'author': comment.author.username,
                'parent_id': comment.parent_id,
                'time_create': comment.time_create.strftime('%Y-%b-%d %H:%M:%S'),
                'avatar': comment.author.profile.avatar.url,
                'content': comment.content,
                'get_absolute_url': comment.author.profile.get_absolute_url()
            }, status=200)

        return redirect(comment.article.get_absolute_url())
    def handle_no_permission(self):
        return JsonResponse({'error': 'Необходимо авторизоваться для добавления комментариев'}, status=400)



















