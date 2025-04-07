from django.contrib import admin
from django.urls import path
from . import views

app_name = 'shop' # название нового файла с путями, чтобы ссылки на страницах находили URL

urlpatterns = [
    # path('', views.ShopHome.as_view(), name='shop'),
    path('admin/', admin.site.urls),
    path('', views.index, name='home_shop'),
    path('cart/<int:id>', views.buy, name='buy'),
    path('cart/', views.toKorz, name='toKorz'),
    path('cart/del/<int:id>', views.delete, name='del'),
    path('cart/pobeda/', views.korzinaZakaz, name='kozinaZakaz'),
    path('cart/count/<str:num>/<int:id>/', views.korzinaCount, name='count'),
    path('toizbran/', views.toizbran, name='toIzbran'),
]