from django.shortcuts import render,redirect
from .form import LogIn,CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request,'base/home.html')

def logUser(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('base/home')
        else:
            messages.success(request,'Your passord or email is incorrect')
            return redirect('base/login')
    else:
        return render(request,'base/login.html')
  

def Register(request):
    Register = CreateUserForm()
    if request.method == 'POST':
        Register = CreateUserForm(request.POST)
        if Register.is_valid():
            Register.save()
    context = {'register':Register}
    return render(request,'base/registration.html',context)