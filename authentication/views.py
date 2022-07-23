from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout  # import des fonctions login, logout et authenticate

from . import forms


def login_page(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('home')
<<<<<<< HEAD
            else:
                message = 'Identifiants invalides.'
=======
        message = 'Identifiants invalides.'
>>>>>>> f3dc60dde3dd6edbe4a2fcebb4307cc0156b0a30
    return render(
        request, 'authentication/login.html', context={'form': form, 'message': message})


def logout_user(request):
    logout(request)
    return redirect('login')


def signup_page(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    return render(request, 'authentication/signup.html', context={'form': form})
