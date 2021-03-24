# Homework 0324

> Django Model Relationship



* Django 1:N Model Relation



## 1. Lookup

지문의 코드에서 '__gt' 부분을 lookup이라고 한다. 링크를 참고하여 Django에서 사용가능한 lookup 세가지와 그 의미를 작성하시오.

https://docs.djangoproject.com/en/3.1/ref/models/querysets/#field-lookups

![image-20210324165425091](Homework 0324.assets/image-20210324165425091.png)



```
__exact

__iexact

__contaions
```





''





## 2. 1:N 관계 설정

지문은 1:N 관계 설정을 하기 위하여 정의된 모델이다. 링크를 참고하여 빈 칸에 들어갈 수 있는 값 세가지를 선택 후 그 의미를 작성하시오.

https://docs.djangoproject.com/en/3.1/ref/models/fields/#arguments

![image-20210324165508706](Homework 0324.assets/image-20210324165508706.png)





## 3. comment create view

지문은 댓글 기능을 작성하기 위한 코드이다. 빈 칸에 들어갈 코드와 의미를 작성하시오.









## 4. 1:N DB API

게시물 아래에 댓글을 출력하려고 한다. Article과 Commnet 모델이 1:N으로 관계설정이 되어 있다고 가정 할 때 아래의 빈칸에 적절한 코드를 작성하시오.

![image-20210324165618012](Homework 0324.assets/image-20210324165618012.png)





```django
comments=article.comment_set.all()
context = {
'comments':comments,
}
```



