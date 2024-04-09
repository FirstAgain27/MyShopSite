
from django.urls import path

from main import views

app_name = 'main'

urlpatterns = [
    path('', views.index,name='index'),
    path('about/',views.about,name='about'),
    path('payment/',views.payment_and_shipping,name='payment'),
    path('cont_inf/',views.cont_inf,name='cont_inf'),
]


