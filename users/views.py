from django.shortcuts import render,redirect
from .forms import CustomRegisterForm
from django.contrib import messages
# Create your views here.

def register(request):
    if request.method == "POST":
       registerform = CustomRegisterForm(request.POST)
       if registerform.is_valid():
           registerform.save()
           messages.success(request, ("New UserAccount Created"))
           return redirect('register')

    else:
        registerform = CustomRegisterForm()
        return render(request, 'register.html', {'registerform': registerform})