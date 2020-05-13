from django.contrib import auth
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render

from django.views.generic.base import View

from .forms import UserCreateForm


def register(request):
    if request.method == 'POST':
        user_form = UserCreateForm(request.POST)

        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.save()
            return HttpResponseRedirect('/')
    else:
        user_form = UserCreateForm()
    return render(request, 'register.html', {'form': user_form})


def logins(request):
    args = {}
    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect('/')
        else:
            args['login_error'] = "Пользователь не найден"
            return render(request, 'login.html', args)
    else:
        return render(request, "login.html", args)


class LogoutFormView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')
