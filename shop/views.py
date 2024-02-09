from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.views.generic import ListView

from clinic.models import Pet


# Create your views here.

# def index(request):
#     return render(request, 'shop_home.html')

class ShopHome(ListView):
    template_name = 'shop_home.html'
    title_page = 'Магазин для ваших питомцев'

    def get_queryset(self): # формирует параметр для пути, открывать выбранную позицию
        return Pet.objects.all()

