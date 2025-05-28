from django.contrib.auth import login, authenticate, logout

from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserLoginForm


def register(request):
    print(request.POST)
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print('erros@@@@@@@@@@', form.errors)
    else:
        form = UserRegisterForm()
    context = {
        'form': form, 
        # 'errors': form.errors
    }
    return render(request, 'register.html', context)

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
    else:
        form = UserLoginForm()
    print('@@@@@@@@@@@', form.errors)
    context = {
        'form': form,
        'errors': form.errors
    }
    return render(request, 'login.html', context)

def user_logout(request):
    logout(request)
    return redirect('accounts:login')