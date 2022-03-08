from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from valetapp.forms.Registration.signup import SignUpForm
from django.contrib.auth import authenticate, login as auth_login

from django.contrib.auth import (
    authenticate,
    login,
    logout
)
from valetapp.forms.Registration.CustomerFactory import CustomerFactory

from valetapp.forms.Registration.StaffFactory import StaffFactory
from valetapp.models.Users.customer import Customer
from valetapp.models.Users.staff import Staff


def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = authenticate(request, username=username, password=password)
            if user and user.is_active:
                auth_login(request, user)
            return redirect('../home/')
    else:
        form = AuthenticationForm()
    return render(request, 'Login/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('../home/')


def register(request):
    if request.method == 'POST':
        
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            email = form.cleaned_data.get('email')

            if "@valetsystem.ie" in email:
                sf = StaffFactory
                staff = Staff(sf)
                staff.create_user(user=user)
            else:
                print(form)
                cf = CustomerFactory
                customer = Customer(factory=cf)
                colour = form.cleaned_data.get('colours')
                print(colour)
                customer.create_user(user=user, colour=colour)

            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'Registration/register.html', {'form': form})
