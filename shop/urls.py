from django.urls import path
from . import views

app_name = 'shop' # название нового файла с путями, чтобы ссылки на страницах находили URL

urlpatterns = [
    path('', views.ShopHome.as_view(), name='shop'),
]