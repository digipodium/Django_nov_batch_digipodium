from django.shortcuts import render
from app.models import *

# Create your views here.
def home(request):
    articles = Article.objects.all()
    # news = ...
    ctx = {
        'articles':articles,
        #'news':news,
    }
    return render(request, "index.html", context=ctx)

def contact(request):
    return render(request, "contact.html", context={})

def about(request):
    return render(request, "about.html", context={})
