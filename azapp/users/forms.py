from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')


class UserDetailChangeForm(forms.ModelForm):
    first_name = forms.CharField(label='First Name',widget=forms.TextInput(attrs={'class':'form-control',}))
    last_name = forms.CharField(label='Last Name',widget=forms.TextInput(attrs={'class':'form-control',}))

    class Meta:
        model = CustomUser
        fields = ['first_name','last_name']
