from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.AccountHomeView.as_view() , name='user_profile' ),
    path('details/', views.UserDetailUpdateView.as_view() , name='account_update' ),
    path('login-signup/', views.login_signup, name='login_signup'),
]
