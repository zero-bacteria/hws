from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):

    articles = Article.objects.all()

    context = {
        'articles' : articles,
    }

    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    if request.method == "POST":
        articles = Article()

        articles.title = request.POST.get('title')
        articles.content = request.POST.get('content')

        articles.save()

    return redirect('articles:detail', articles.pk)

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    
    context = {
        'article' : article,
    }
    return render(request, 'articles/detail.html', context)

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/edit.html', context)

def update(request, pk):

    article = Article.objects.get(pk=pk)

    article.title = request.POST.get('title')
    article.content = request.POST.get('content')

    article.save()

    return redirect('articles:detail', article.pk)

def delete(request, pk):

    article = Article.objects.get(pk=pk)

    article.delete()

    return redirect('articles:index')

    

