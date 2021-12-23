from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    categories = Category.objects.all()
    articles = Article.objects.all()

    ctx = {
        'articles': articles,
        'categories' : categories,
    }

    return render(request, 'index.html', ctx)