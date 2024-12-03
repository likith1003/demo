from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import *
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.core.mail import send_mail

def home(request):
    return render(request, 'home.html')



def register(request):
    EUFO = UserForm()
    EIFO = InfoForm()
    d = {'EUFO': EUFO, 'EIFO': EIFO}
    if request.method == 'POST':
        UFDO = UserForm(request.POST)
        IFDO = InfoForm(request.POST)
        if UFDO.is_valid() and IFDO.is_valid():
            pw = UFDO.cleaned_data.get('password')
            MUFDO = UFDO.save(commit=False)
            MUFDO.username = UFDO.cleaned_data.get('email')
            MUFDO.set_password(pw)
            MPFDO = IFDO.save(commit=False)
            MPFDO.username = MUFDO
            role = IFDO.cleaned_data.get('Role')
            if role in ('Owner', 'Director'):
                MUFDO.is_staff = True
                MUFDO.is_superuser = True
            MUFDO.save()
            MPFDO.save()
            
            # Send email to the registered email address
            subject = 'Welcome to Our Website!'
            message = 'Thank you for registering with us.'
            from_email = 'shrabantidas97@gmail.com'
            recipient_list = [MUFDO.email]
            send_mail(subject, message, from_email, recipient_list)
            
            return HttpResponse('User Registration Is successful')
        return HttpResponse('Invalid data')
    return render(request, 'register.html', d)



def user_login(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        un = request.POST.get('un')
        pw = request.POST.get('pw')
        user = authenticate(username=un, password=pw)
        if user and user.is_active:
            auth_login(request, user)
            request.session['username'] = un
            print('hiiii hello ')
            return HttpResponseRedirect(reverse('home'))
        messages.error(request, 'Invalid credentials')

    return render(request, 'user_login.html') 


