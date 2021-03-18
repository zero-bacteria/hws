# Workshop 0317

> Static/Media



* Django Web Framework
* Media File
* Django Media File과 HTML form





## 1. Media file with HTML input

![image-20210318124331404](Workshop 0317.assets/image-20210318124331404.png)



1) < input type="file" > 태그를 사용할 경우 반드시 사용해야 하는 enctype 속성 값 (a) 를 작성하시오



```django
enctype="multipart/form-data"
```





2) accept 속성은 파일 업로드 제어에서 선택할 수 있는 파일 유형을 정의하는 속성이며 input 태그의 type이 file일 경우에만 유효하다.

예를 들어 표준 비디오 형식 뿐만 아니라 PDF 파일도 받을 수 있어야 할 때, 빈칸 (b)에 들어갈 알맞은 속성 값을 작성하시오.



```
(b) video/* , .PDF
```



pdf의 경우 마지막 형식자 pdf만 받겠다는 의미

