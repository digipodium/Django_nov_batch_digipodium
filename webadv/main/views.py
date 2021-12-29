from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q

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

def article_search(request):
    query = request.GET.get('q')
    if query:
        # qdate = request.GET.get('year',2020)
        # search about query in article
        results = Article.objects.filter(Q(title__icontains=query)|Q(content__icontains=query))
        # date_results = Article.objects.filter(date__year=int(qdate))
        # results should be displayed on a page
        ctx= {
            'results':results,
            'query': query,
            'result_count': len(results),
            # 'date_results':date_results,
        }
        return render(request,'article_search.html',ctx)
    else:
        return redirect('index')