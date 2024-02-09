# копия urls, который находится непосредственно в приложении, а в основном urls стоит ссылка на этот файл, зачем это нужно пока непонятно, но вроде как нужно
from django.contrib import admin
from django.urls import path, re_path, register_converter, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls), # путь для кабинета администратора

    path('', views.PetHome.as_view(), name='home'),
    # path('veterinarian/', views.veterinarian, name='vet'),

    path('pet/', views.Pet_list.as_view(), name='allpet'),
    path('pet/<slug:pk>/<str:slugPet>', views.Pet_detail.as_view(), name='info_pet'),

    path('vet/', views.Veterinarian_list.as_view(), name='allvet'),
    path('vet/<slug:pk>/<str:slugVet>', views.Veterinarian_detail.as_view(), name='info_vet'),

    path('record/', views.record, name='record'),

    path('user_pet/', include('django.contrib.auth.urls')), # чтобы юзеры могли заходить на сайт в кабинет за счет переадресации include
    # path('user_pet/registration/', views.registration, name='registration'),

    path('edit_a_profile/', views.AddEdit_a_profile.as_view(), name='edit_a_profile'),

    path('services/', views.services, name='services')
]
