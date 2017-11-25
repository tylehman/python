# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

@login_required
def home1(request):
    return render(request, 'user_account/home1.html')

def signup(request):
    if request.method== "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home1')

    else:
        form = UserCreationForm()
    return render(request, 'user_account/signup.html', {'form' : form })
