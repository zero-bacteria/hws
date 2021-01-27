# Homework 0127

> 객체 지향 프로그래밍



* 클래스, 인스턴스, 메서드
* 모듈



## 1. Type Class

Python은 객체 지향 프로그래밍 언어이다. Python에서 기본적으로 정의되어 있는 클래스를 최소 5가지 이상 작성하시오.



int , list , set, tuple, dict



## 2. Magic Method

아래에 제시된 매직 메서드들이 각각 어떠한 역할을 하는지 간단하게 작성하시오.

```python
__init__, __del__, __str__, __repr__
```

`__init__` 인스턴스가 생성될 때 인스턴스의 속성을 정의 할 수 있다.

`__ del__` 인스턴스 객체가 소멸 되기 직전에 호출된다.

`__str__` 객체를 출력할때 자동으로 보여줄 내용을 정의 할 수 있다.

`__repr__` 객체를 출력할때 사람이 볼 수 있는 문자열 형태로 출력해줌?



## 3. Instance Method

.sort()와 같이 문자열, 리스트, 딕셔너리 등을 조작 할 때 사용하였던 것들은 클래스에 정의된 메서드들이었다. 이처럼 문자열, 리스트, 딕셔너리 등을 조작하는 메서드를 최소 3가지 이상 그 역할과 함께 작성하시오.



`.count()` 리스트에서 해당하는 요소의 갯수를 반환해줌

`.upper()` 해당 문자열을 대문자로 변환해줌

`isalpha()` 문자로만 이루어졌는지 판단해줌



## 4. Module Import

```python
# fibo.py

def fibo_recursion(n):
    if n < 2:
        return n
    else:
        return fibo_recursion(n-1)+fibo_recursion(n-2)
```

위와 같은 코드가 같은 폴더 안의 fibo.py 파일에 작성되어 있을 때, 아래와 같은 형태로 함수를 실행 할 수 있도록 하는 import 문을 빈칸 (a), (b), (c)를 채워 넣어 완성하시오.

```python
from __(a)__ import __(b)__ as __(c)__

recursion(4)
```

(a) fibo

(b) fibo_recursion

(c) recursion



