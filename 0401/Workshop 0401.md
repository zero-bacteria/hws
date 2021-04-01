# Workshop 0401

> Django Model Relationship



* Web Framework
* Django
* 팔로우 기능 구현





## Django Project

데이터베이스 M:N 관계를 활용하여 팔로우 기능을 구현하시오.





## 1. Model & Form

팔로우 기능을 구현하기 위한 모델을 세팅한다.

팔로우 기능을 구현하기 위해 User 모델을 대체한다.





## 2. url & view

/accounts/<username>/

유저 프로필 페이지 기능을 구현한다.

* 로그인한 유저만 팔로우를 할 수 있다.



/accounts/<username>/follow/

팔로우를 하기 위한 기능을 구현한다

* 로그인한 유저만 팔로우를 할 수 있다
* 본인은 팔로우를 할 수 없다





## 3. template

index.html의 username 에 profile 로 갈 수 있는 링크를 설정한다 .

팔로잉 여부에 따라 팔로우와 언팔로우 버튼이 토글될 수 있도록 구성한다.

* 로그인한 유저 자신의 프로필 페이지에서는 팔로우 & 언팔로우 버튼이 보이지 않는다
* 작성자의 팔로잉 , 팔로워 숫자를 보여주고 유저의 이름을 모두 출력한다

(선택 ) 해당 프로필의 유저가 작성한 모든 글의 내용과 좋아요 숫자를 보여준다

