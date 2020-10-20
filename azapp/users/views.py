from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import DetailView,  UpdateView, FormView
from django.urls import reverse_lazy
from allauth.account.forms import LoginForm,  SignupForm



from .forms import UserDetailChangeForm

class AccountHomeView(LoginRequiredMixin,DetailView):
    template_name = 'account/home.html'

    def get_object(self):
        return self.request.user
    def get_context_data(self , **kwargs):
        context = super(AccountHomeView, self).get_context_data(**kwargs)


        context['active'] = "account"

        return context


def login_signup(request):
    data = {
    'form1': LoginForm,
    'form2': SignupForm,
    }
    return render(request, 'account/login_signup.html', data)

class UserDetailUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    form_class = UserDetailChangeForm
    template_name = 'account/account_edit.html'
    success_url = reverse_lazy("users:user_profile")
    success_message = 'Profile successfully updated '
    def get_object(self):
        return self.request.user





def update_user_details(request):
    user = request.user
    new_email = request.POST.get('new_email')
    user.custom_user.add_email_address(request, new_email)

