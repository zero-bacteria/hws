# Homework 0318

> Static/Media



* Django Web Framework
* Static File
* Django Static File 관리의 이해







## 1. Compiled Bootstrap

CSS, JS 파일을 다운로드 받아 Django 프로젝트에 Static 파일로 추가하시오
부트스트랩이 적용되기 위해 작성해야 할 코드를 제출하시오
https://getbootstrap.com/docs/5.0/getting-started/download/





1. crud/static/stylesheets 경로 만들기
   1. 부트스트랩 css 파일넣기
   2. 부트스트랩 js 파일넣기
2. base.html 에

```django
{% load static %}

<link rel="stylesheet" href="{% static 'stylesheets/bootstrap.css' %}">


<script src="{% static 'javascript/bootstrap.js' %}"></script>

```

3.  crud/ settings.py
   1. STATICFILES_DIRS=[ BASE_DIR / 'crud' / 'static']