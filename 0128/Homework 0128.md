# Homework 0128

> 객체 지향 프로그래밍



* 클래스, 인스턴스, 메서드
* 오류와 예외처리



## 1. Circle 인스턴스 만들기

아래와 같은 Circle 클래스가 있을 대, 반지름이 3이고 x,y좌표가 (2,4)인 Circle 인스턴스를 만들어 넓이와 둘레를 출력하시오.



```python
class Circle:
    pi = 3.14
    x = 0
    y = 0
    r = 0
    
    def __init__(self, r, x, y):
        self.r=r
        self.x=x
        self.y=y

    def area(self):
        return self.pi * self.r * self.r

    def circumference(self):
        return 2 * self.pi * self.r

    def center(self):
        return (self.x, self.y)    
```

```python
c1 = Circle(3,2,4)

print(c1.area())
print(c1.circumference())
```

```python
28.259999999999998
18.84
```







## 2. Dog과 Bird는 Animal이다

다음과 같이 Animal클래스가 주어질 때, 해당 클래스를 상속 받아 아래의 보기와 같이 동작하는 Dog 클래스와 Bird 클래스를 작성하시오.



```python
class Animal:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print(f'{self.name}! 걷는다!')

    def eat(self):
        print(f'{self.name}! 먹는다!')
```

```python
dog = Dog('멍멍이')
dog.walk() # 멍멍이! 달린다!
dog.bark() # 멍멍이! 짖는다!

bird = Bird('구구')
bird.walk() # 구구! 걷는다!
bird.eat() # 구구! 먹는다!
bird.fly() # 구구! 푸드덕!
```



```python
class Animal:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print(f'{self.name}! 걷는다!')

    def eat(self):
        print(f'{self.name}! 먹는다!')

class Dog(Animal):

    def walk(self):
        print(f'{self.name}! 달린다!')

    def bark(self):
        print(f'{self.name}! 짖는다!')


class Bird(Animal):

    def fly(self):
        print(f'{self.name}! 푸드덕!')



dog = Dog('멍멍이')
dog.walk() # 멍멍이! 달린다!
dog.bark() # 멍멍이! 짖는다!

bird = Bird('구구')
bird.walk() # 구구! 걷는다!
bird.eat() # 구구! 먹는다!
bird.fly() # 구구! 푸드덕!
```





## 3. 오류의 종류

아래에 제시된 오류들이 각각 어떠한 경우에 발생하는지 간단하게 작성하시오.

```
ZeroDivisionError, NameError, TypeError, IndexError,
KeyError, ModuleNotFoundError, ImportError
```

`ZeroDivisionError` 0으로 나누었을 때

`NameError` 정의된 변수가 없을 때 

`TypeError` 타입이 맞지 않을 때

`IndexError` 인덱스 범위를 벗어났을 때

`KeyError` 키가 존재하지 않을 때

`ModuleNotFoundError`  해당 모듈을 찾지 못했을 때

`ImportError`  임포트를 했을때 오류가 발생했을 때 



