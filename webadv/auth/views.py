from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, RegisterForm
from django.contrib import messages

# Create your views here.
def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Login Successfull")
                return redirect('index')
            else:
                messages.error(request,"Invalid Credentials")
        else:
            messages.error(request,"Error Validating the Form")
    ctx = {
        'form':form,
    }
    return render(request, 'accounts/login.html',ctx)


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST) # filled form
        if form.is_valid():
            form.save() # db me user created
            messages.success(request, "Account Created Successfully")
            return redirect('login')
        else:
           messages.error(request, "Invalid form details")
    else:
        form = RegisterForm() # blank form
    ctx = {
        'form': form
    }

    return render(request, 'accounts/register.html', ctx)