from django.urls import path ,include
from . import views

app_name = 'carts'

urlpatterns = [
    path('', views.cart_home , name='cart' ),
    path('add/', views.cart_add , name='add' ),
    path('remove/', views.cart_remove , name='remove' ),
    path('update/', views.cart_update , name='update' ),
    path('checkout/', views.index, name='checkout'),
    path('charge/', views.charge, name='charge'),
    path('success<str:args>/', views.success, name='success')

]
