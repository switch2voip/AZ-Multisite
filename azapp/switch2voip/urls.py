from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from . import views

app_name = 'switch2voip'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('shop/', views.ProductListView.as_view() , name='product_list' ),
    path('<slug>/', views.ProductCategory.as_view() , name='product_list_by_category' ),
    path('<id>/<slug>/', views.ProductDetailView.as_view() , name='product_detail' ),
]
