"""Veterinary_clinic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from Veterinary_clinic import settings
from clinic.views import page_not_found
from clinic import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('clinic.urls')),
    path('users/', include('users.urls', namespace='users')), # перенаправка на другой urls связанный с авторизацией на сайте, 2-й параметр обязателен для полей имен
    # path("__debug__/", include("debug_toolbar.urls")),  # для джангодебага
]

if settings.DEBUG: # чтобы в режиме отладки в кабинете администратора к маршруту добавлялась префикс медиа
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# обработчик если страница не опреледена сама функция во вьюхе
handler404 = page_not_found

admin.site.site_header = 'Панель администрирования'  # замена в кабинете админа заголовка
admin.site.index_title = 'Ветеринарная клиника'  # замена в кабинете админа заголовка









