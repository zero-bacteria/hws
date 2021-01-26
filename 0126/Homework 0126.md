# Homework 0126

> 데이터 구조 및 활용



* 데이터 구조

* 메서드

  



## 1. Built-in 함수와 메서드

**sorted()** 와 **.sort**의 차이점을 코드의 실행 결과를 활용하여 설명하시오.



```python
list_a = [1,3,2,4]

b= sorted(a)

print(a)
print(b)

a.sort()

print(a)
print(b)
```

```bash
$ python p1.py
[1, 3, 2, 4]
[1, 2, 3, 4]
[1, 2, 3, 4]
[1, 2, 3, 4]
```

* sorted 내장 함수로 return 값이 있고 원본을 건드리지 않는다.
* sort는 메서드로 원본이 변경된다.





## 2. extend()와 .append()

.extend() 와 . append의 차이점을 코드의 실행 결과를 활용하여 설명하시오



```python
a= ['apple']

a.append('banana')

a.extend('banana')
```

```python
a = ['apple', 'banana']

a = ['apple', 'b','a','n','a','n','a']
```

* `.append()`는 리스트에 값을 추가해줌
* `.extend()`는 리스트에 리스트 값들을 각각 추가해줌





## 3. 복사가 잘 된 건가?

아래의 코드를 실행 하였을 때, 변수 a와 b가 담긴 list의 요소가 같은지 혹은 다른지 여부를 판단하고 그 이유를 작성하시오.



```python
a = [1,2,3,4,5]
b = a

a[2] = 5

print(a)
print(b)
```

* **같다**

  그 이유는 리스트가 저장될때 같은 위치에 저장되기 때문에 일반복사를 진행하고 원본의 리스트를 바꾼다면 복사본의 리스트 역시 바뀌게 된다. 이를 피하기 위해서는 shallow copy혹은 상황에 따라서 deepcopy 방법을 사용하여야 한다.

  







