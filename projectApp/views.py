from django.shortcuts import render,redirect
from .form import LogIn
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request,'base/home.html')

# def logUser(request):
#     if request.method == 'POST':
#         username = request.POST["username"]
#         password = request.POST["password"]
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('login_success')
#         else:
#             messages.success(request,'Your passord or email is incorrect')
#             return redirect('login_success')
#     else:
#         return render(request,'base/login.html')
  
# def LoginSuccess(request):
#     return render(request, 'base/login_success.html')

def logUser(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('login_successful.html')
        else:
            messages.success(request,'You are successfully logged in ')
            return redirect('login')
    else:
        return render(request,'base/login.html')

def Register(request):
    if request.method == 'POST':
        Register = UserCreationForm(request.POST)
        if Register.is_valid():
            Register.save()
            username = Register.cleaned_data['username']
            password = Register.cleaned_data['password1']
            user = authenticate(usernae = username,password =password)
            login(request,user)
            messages.success(request,('Registered successfully'))
            return redirect('home')
    else:
        Register = UserCreationForm()
    context = {'form':Register}
    return render(request,'base/registration.html',context)