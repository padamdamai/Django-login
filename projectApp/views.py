from django.shortcuts import render,redirect
from .form import LogIn,CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def home(request):
    return render(request,'base/home.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username= username,password = password)

        if user is not None:
            LogIn(request,user)
            return redirect('base/home')
    context = {}
    return render(request,'base/login.html',context)

def Register(request):
    Register = CreateUserForm()
    if request.method == 'POST':
        Register = CreateUserForm(request.POST)
        if Register.is_valid():
            Register.save()
    context = {'register':Register}
    return render(request,'base/registration.html',context)