from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.

def index(request):
    return render(request,'index.html')

def login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('new_page')
        else:
            messages.info(request,'wrong credentials')
            return redirect('login')
    return render(request,'login.html')

def register(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']

        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username taken')
                return redirect('register')

            else:
                user=User.objects.create_user(username=username,password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request,'Password Is Not Matching')
            return redirect('register')
        print('User created')
        return redirect('/')
    return render(request,'register.html')

def new_page(request):
    return render(request,'new_page.html')

def new_form(request):
    if request.method=='POST':
        messages.info(request,'Application accepted')
    return render(request,'new_form.html')

def logout(request):
    auth.logout(request)
    return redirect('/')