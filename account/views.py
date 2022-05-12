from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm

# Create your views here.

def register_user(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = authenticate(request,username=username,email=email,password=password)
            login(request,user)
            messages.success(request,"You have been registered successfully!")
            return redirect("/")
    else:
        form = RegisterForm()

    return render(request,'registration/register.html',{
        'form':form
    })

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"You have been loggedin successfully!")
            return redirect("/")
        else:
            messages.error(request,"Something went wrong please try again")
            return redirect("/account/login")
    else:
        return render(request,'registration/login.html')

def logout_user(request):
    logout(request)
    messages.success(request,"Logout successfully!")
    return redirect("/account/login")
