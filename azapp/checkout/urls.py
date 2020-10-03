from django.contrib import admin
from django.urls import path, include
from . import views


app_name = 'checkout'

urlpatterns = [

    path('',views.index,name='index'),
    # path('payment/',views.payment,name='payment'),
    path('success/<str:args>/',views.success,name='success'),
    path('charge/',views.charge, name='Charge'),

]
