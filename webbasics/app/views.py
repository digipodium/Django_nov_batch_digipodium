from django.shortcuts import redirect, render
from app.models import *
from .forms import *
from django.contrib import messages

# Create your views here.
def home(request):
    articles = Article.objects.all()
    newslist = News.objects.all()
    ctx = {
        'articles':articles,
        'news':newslist,
    }
    return render(request, "index.html", context=ctx)

def contact(request):
    form = ContactForm()                        # blank form creation
    if request.method == "POST":                # agar form bhar diya
        form = ContactForm(request.POST)        # form create kro but user k input k sath
        if form.is_valid():                     # agar sab badiya
            form.save()                         # save the information to database
            messages.success(request, "Thank you for your message.")
            return redirect('/contact')         # reload the page or goto some page
    ctx ={
        'form': form
    }
    return render(request, "contact.html", context=ctx)

def about(request):
    return render(request, "about.html", context={})
