from django.shortcuts import render, redirect
from django.views.decorators.http import require_safe, require_http_methods, require_POST
from .models import Article
from .forms import ArticleForm
# Create your views here.

@require_safe
def index(request):
    # 모든 게시글을 거꾸로 조회

    articles = Article.objects.order_by('-pk')
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


@require_http_methods(['GET', 'POST'])
def create(request):
    # POST일 때
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    # GET일 때
    else:
        form = ArticleForm()
    context = {
        # 상황에 따른 2가지 모습
        # 1. is_valid에서 내려온 form : 에러메세지를 포함한 form
        # 2. else에서 내려온 form : 빈 form
        'form': form,
    }
    return render(request, 'articles/create.html', context)

@require_safe
def detail(request, pk):
    # 몇번 글을 조회할건지 가져와야 함
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


@require_POST
def delete(request, pk):
    # 삭제할 게시글 조회
    article = Article.objects.get(pk=pk)
    # 삭제 요청이 POST면 삭제, POST가 아니라면 DETAIL 페이지로 redirect
    article.delete()
    return redirect('articles:index')


@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = Article.objects.get(pk=pk)
    # update
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    # edit
    else:
        form = ArticleForm(instance=article)
    context = {
        'form': form,
        'article': article,
    }
    return render(request, 'articles/update.html', context)