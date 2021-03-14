# Workshop 0311

> Model



* Web Framework
* Django Model
* Django CRUD



## Django Project

CRUD를 모두 갖춘 장고 프로젝트를 제작하고 결과 사진과 코드를 별도의 마크다운 파일에 작성하여 제출하시오 .



## 기본설정

1) 프로젝트 이름은 crud, 앱 이름은 articles 로 설정한다.

2) 모든 템플릿에서 상속받아 사용할 base.html 을 작성한다 .

base.html 이 담긴 templates 디렉토리는 프로젝트 및 앱 디렉토리와 동일한 위치에 생성한다.

base.html 은 Bootstrap CDN 을 포함하고 있어야 한다 .



## CRUD 구현

제시된 결과 사진들을 참고하여 장고 프로젝트를 진행하시오.



1. Read

   ![image-20210314154414719](Workshop 0311.assets/image-20210314154414719.png)

2. Create

   작성을 완료하면 해당 게시글의 상세 페이지로 이동한다.

   ![image-20210314154419882](Workshop 0311.assets/image-20210314154419882.png)

3. Detail

   ![image-20210314154423911](Workshop 0311.assets/image-20210314154423911.png)

4. Update

   작성을 완료하면 해당 게시글의 상세 페이지로 이동한다.

   ![image-20210314154428953](Workshop 0311.assets/image-20210314154428953.png)

5. Delete

   별도 페이지 없음





## 결과

![image-20210314162817010](Workshop 0311.assets/image-20210314162817010.png)



![image-20210314162854158](Workshop 0311.assets/image-20210314162854158.png)

![image-20210314162930188](Workshop 0311.assets/image-20210314162930188.png)

![image-20210314162946798](Workshop 0311.assets/image-20210314162946798.png)



**articles/**



urls.py

```python
from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/delete/', views.delete, name='delete'),

]
```



views.py

```python
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

```





**articles/templates/articles/**



index.html

```django
{% extends 'base.html' %}

{% block content %}

  <h1>INDEX</h1>
  
  <a href="{% url 'articles:new' %}">NEW</a>
  <br>
  
  {% for article in articles %}
  <br>
  <h2>제목: {{ article.title}}</h2>
  <p>내용: {{ article.content }}</p>
  <a href="{% url 'articles:detail' article.pk %}">DETAIL</a>
  <br>
  <br>
  {% endfor %}

  
{% endblock  %}
```



new.html

```django
{% extends 'base.html' %}

{% block content %}
  <h1>NEW</h1>

  <form action="{% url 'articles:create' %}" method="POST">
    {% csrf_token %}
    <label for="title">TITLE:</label>
    <input type="text" id="title" name="title"><br>
    <label for="content">CONTENT:</label>
    <textarea name="content" id="content" cols="30" rows="10"></textarea><br>
    <input type="submit" value="작성">
  
  </form>

  <a href="{% url 'articles:index' %}">BACK</a>
  

{% endblock  %}
```





detail.html

```django
{% extends 'base.html' %}

{% block content %}
<h1>DETAIL</h1>
<hr>
<h2>{{ article.title }}</h2>
<p>{{ article.content }}</p>
<p>작성일: {{ article.created_at }}</p>
<p>수정일:{{ article.updated_at }}</p>

<a href="{% url 'articles:edit' article.pk %}">EDIT</a>
<a href="{% url 'articles:delete' article.pk %}">DELETE</a>
<br>

<a href="{% url 'articles:index' %}">BACK</a>
{% endblock  %}
```



edit.html

```django
{% extends 'base.html' %}

{% block content %}
<h1>EDIT</h1>
<form action="{% url 'articles:update' article.pk %}" method="POST">
    {% csrf_token %}
    <label for="title">TITLE</label>
    <input type="text" id="title" name="title" value="{{ article.title }}"><br>
    <label for="content">CONTENT </label>
    <textarea name="content" id="content" cols="30" rows="10">{{ article.content }}</textarea><br>
    <input type="submit" value="수정">
</form>

<a href="{% url 'articles:index' %}">BACK</a>

{% endblock  %}
```

