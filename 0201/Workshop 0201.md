# Workshop 0201

> HTML & CSS



* HTML
* CSS
* HTML tag의 이해
* CSS Selector의 이해



## 1. img tag

아래 그림과 같은 폴더 구조가 있다. resume.html에서 코드를 작성 중일 때, image폴더 안의 my_photo.png를 보여주는 <img> tag를 작성하시오.

단, 이미지가 제대로 출력되지 않을 때는 ssafy 문자열이 출력 되도록 작성하시오.

![image-20210202170123019](Workshop 0201.assets/image-20210202170123019.png)



![image-20210202170129518](Workshop 0201.assets/image-20210202170129518.png)

```html
<img src="C:\Users\user\Desktop\SSAFY 코딩\hws\0201" alt="ssafy">
```





## 2. 파일 경로

위와 같이 경로를 (a)로 작성 할 시, github에 업로드 하거나 전체 폴더의 위치가 변경 되었을 때 이미지를 불러 올 수 없게 된다. 이를 해결 하려면 이미지 경로를 (b)로 바꾸어 작성하면 된다.

(a)와 (b)에 들어갈 말과 (b)로 변경한 코드를 작성하시오.



(a) 절대경로

(b)상대경로 ( 동일한 폴더에 위치할 때)

```html
<img src="my_photo.png" alt="ssafy">
```

/my_photo.png"







## 3. Hyper Link

출력된 my_photo.png 이미지를 클릭하면 ssafy.com으로 이동하도록 하시오.



```html
<a href="https://www.ssafy.com">
      <img src="my_photo.png" alt="ssafy">
</a>
```





## 4. 선택자

1) 아래의 코드를 작성하고 결과를 확인 하시오.

![image-20210202170206213](Workshop 0201.assets/image-20210202170206213.png)

![image-20210202170214572](Workshop 0201.assets/image-20210202170214572.png)





2) nth-child를 nth-of-type으로 변경하고 결과를 확인하시오.

![image-20210202170225125](Workshop 0201.assets/image-20210202170225125.png)



(1),(2) 결과

![제목 없음](Workshop 0201.assets/제목 없음.png)



3) 작성한 코드를 참고하여 nth-child( )와 nth-of-type( )의 차이점을 작성하시오. 



nth-child( ) 모든 자식요소 중 n번째 요소



 nth-of-type( ) 부모의 특정 자식 중 2번째 요소 





