# Create your views here.

# class ShopHome(ListView):
#     template_name = 'shop_home.html'
#     title_page = 'Магазин для ваших питомцев'
#
#     def get_queryset(self):  # формирует параметр для пути, открывать выбранную позицию
#         return Pet.objects.all()

from django.http import JsonResponse
from django.shortcuts import render, redirect

from .forms import *
from .models import *


def index(req):
    items = Tovar.objects.all()
    items2 = Izbran.objects.all()
    data = {'tovari': items, 'izbrannie': items2}
    # delete(req, id)
    return render(req, 'shop_home.html', data)


def buy(request, id):
    item = Tovar.objects.get(id=id)
    item.vkorzine = True
    item.save()
    user = request.user
    print(id, user)
    print(request.session.session_key)
    if user.username:
        if Korzina.objects.filter(tovar_id=id, user_id=user.id):
            getTovar = Korzina.objects.get(tovar_id=id)
            getTovar.count += 1
            getTovar.summa = getTovar.calcSumma()
            getTovar.save()
        else:
            Korzina.objects.create(count=1, tovar=item, summa=item.price, user=user)
    else:
        # newuser = User.objects.create_user(username='Tempuser')
        # if Korzina.objects.filter(tovar_id=id, user_id__isnull=True):
        #     getTovar = Korzina.objects.get(tovar_id=id)
        #     getTovar.count+=1
        #     getTovar.summa = getTovar.calcSumma()
        #     getTovar.save()
        # else:
        Korzina.objects.create(count=1, tovar=item, summa=item.price)
    return redirect('shop:home_shop')


def toKorz(req):
    items = Korzina.objects.filter(user_id=req.user.id)
    myform = Myforms()
    itog = 0
    for i in items:
        itog += i.calcSumma()
    data = {'items': items, 'itog': itog, 'myform': myform}
    return render(req, 'korzina.html', data)


def delete(request, id):
    item = Korzina.objects.get(id=id)
    item.delete()
    return redirect('toKorz')


from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import requests
@method_decorator(csrf_exempt)
def korzinaZakaz(req):
    print('1')
    if req.POST:
        print('2')
        adres = req.POST.get('k1')
        name = req.POST.get('k2')
        tel = req.POST.get('k3')
        # print(adres)
        items = Korzina.objects.filter(user_id=req.user.id)
        samzakaz=''
        for one in items:
            samzakaz+= one.tovar.opis+' '+str(one.count)+' '+str(one.summa)+'\n'
        itog = 0
        for i in items:
            itog += i.summa
        Zakaznew.objects.create(adres=adres, name=name, tel=tel, total=itog,
                                samzakaz=samzakaz)
        items.delete()
        ####################################################################
        TOKEN = "6154094275:AAG1_hHM612EKjhE33o7dq0D8uWdDAYWVFs"
        chat_id = "1485457829"
        message = samzakaz + adres +' '+ name +' '+ tel
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
        print(requests.get(url).json())  # Эта строка отсылает сообщение
        #######################################################################
        return JsonResponse({'mes':'data success','link':'../'})
    return redirect('home')
#https://api.telegram.org/botTOKEN/getUpdates

def korzinaCount(req, num, id):
    tovar = Korzina.objects.get(id=id)
    print(num, id)
    tovar.count += int(num)
    # if tovar.count<0:
    #     tovar.count=0
    # tovar.delete()
    tovar.save()
    if tovar.count < 0:
        tovar.count = 0
        tovar.delete()
    return redirect('toKorz')


@method_decorator(csrf_exempt)
def toizbran(req):
    print('123')
    if req.POST:
        k1 = req.POST.get('k1')
        k2 = req.POST.get('k2')
        print(k1, k2)
        # item = Tovar.objects.get(id=k1)
        if Izbran.objects.filter(tovar_id=k1):
            item = Izbran.objects.get(tovar_id=k1)
            item.delete()
        else:
            Izbran.objects.create(tovar_id=k1)

        return JsonResponse({'mes': 'data success', 'link': ''})
    return redirect('home')
