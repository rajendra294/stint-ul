from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from .forms import CustomRegisterForm

def register(request):
    if request.method == "POST":
        register_form = CustomRegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, "New User Account Created, Login To Started!")
            return redirect('login')  # Redirect to login page after registration
    else:
        register_form = CustomRegisterForm()
    return render(request, 'register.html', {'register_form': register_form})

def logout_view(request):
    logout(request)
    return redirect('login')
