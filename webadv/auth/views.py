from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm

# Create your views here.
def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                msg = "Invalid Credentials"
        else:
            msg = "Error Validating the form"
    ctx = {
        'form':form,
        'msg' : msg,
    }
    return render(request, 'accounts/login.html',ctx)

def register_view(request):
    pass