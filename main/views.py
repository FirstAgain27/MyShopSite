from django.http import HttpResponse
from django.shortcuts import render 


from goods.models import Categories

def index(request):

    context = {
        'title' : 'Home - Главная',
        'content' : 'Магазин мебели HOME',
        }
    
    return render(request,'main/index.html',context)

def about(request):
    context = {
        'title' : 'Home - О нас',
        'content' : 'О нас',
        'text_on_page' : 'Текст о том,какой этот магазин классный'
    }
    
    return render(request,'main/about.html',context)

def payment_and_shipping(request):
    context = {
        'title' : 'Страница для оплаты и доставки товара',
        'text_page' : 'На этой странице осуществляется оплата и доставка товара',
    }

    return render(request,'main/payment_and_shipping.html',context)

def cont_inf(request):
    context = {
        'title' : 'Страница с контактной информацией',
        'text_on_page' : 'На этой странице,вы всегда сможете найти наши контакты',
    }

    return render(request,'main/cont_inf.html',context)




    
