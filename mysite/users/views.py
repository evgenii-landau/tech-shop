from django.shortcuts import render

from django.contrib.auth import authenticate
from .forms import LoginUserForm
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout

from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = "users/login.html"
    extra_context = {"title": "Авторизация"}


# def logout_user(request):
#     logout(request)
#     return HttpResponseRedirect(reverse("users:login"))
