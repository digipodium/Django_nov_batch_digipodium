from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    categories = Category.objects.all()
    filter_cat = request.GET.get('c',0)
    filter_author = request.GET.get('a')
    if filter_cat:
        articles = Article.objects.filter(category = filter_cat)
    elif filter_author:
        articles = Article.objects.filter(user = filter_author)
    else:
        articles = Article.objects.all()

    ctx = {
        'articles': articles,
        'categories' : categories,
        'fc': int(filter_cat),
    }

    return render(request, 'index.html', ctx)

def article_detail(request,id):
    article = Article.objects.get(id=id)
    ctx ={
        'data': article
    }
    return render(request,'article_details.html',ctx)