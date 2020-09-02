"""azapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import  settings
from django.conf.urls.static import  static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('super-admin/', admin.site.urls),
    path('accounts/login/', auth_views.LoginView.as_view()),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('apps.core.urls')),
    path('blog/', include('apps.blog.urls')),
    path('faqs/', include('apps.faq.urls')),
    path('product/', include('apps.carty.urls')),
    path('cart/', include('apps.cart.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)