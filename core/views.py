from django.shortcuts import render, HttpResponseRedirect
from .forms import LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def home(request):
    return render(request, 'core/home.html', {'home': 'active'})

def skill(request):
    return render(request, 'core/skills.html', {'skill': 'active'})

def contact(request):
    return render(request, 'core/contact.html', {'contact': 'active'})

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in Successfully !!')
                    return HttpResponseRedirect('/')
        else:
            form = LoginForm()
        return render(request, 'core/login.html', context={'form': form, 'user_login': 'active'})
    else:
        return HttpResponseRedirect('/')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')    