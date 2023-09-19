from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from common.forms.user import RegisterUserForm, LoginUserForm


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'common/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('profile')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'common/login.html'

    def get_success_url(self):
        return reverse_lazy('profile')


def profile(request, **kwargs):
    kwargs.update({'title': 'Профиль'})
    return render(request, 'common/profile.html', kwargs)


def logout_user(request, **kwargs):
    logout(request)
    return redirect('login')
