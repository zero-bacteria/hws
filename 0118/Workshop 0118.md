# 1월 18일 Wokrshop

* 데이터의 입력 및 출력
* 제어문
* python 프로그래밍 언어 기본 문법의 이해
* 데이터 입출력 방법의 이해





## 1. 세로로 출력하기	

​	자연수 number를 입력 받아, 1부터 number까지의 수를 세로로 한줄씩 출력하시오.

```python
n=int(input())

for n in range(1,n+1):
    print(n)
```



## 2. 거꾸로 세로로 출력하기

​	자연수 number를 입력 받아, number부터 0까지의 수를 세로로 한줄씩 출력하시오.

```python
number = int(input())

for n in range(0,number+1):
    
    print(number)
    number-=1
	
```



## 3. N줄 덧셈 (SWEA # 2025)

입력으로 자연수 number가 주어질 때, 1부터 주어진 자연수 number까지를 모두 더한 값 을 출력하시오. 단, 주어지는 숫자는 10000을 넘지 않는다. 예를 들어, 주어진 숫자가 10일 경우 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55이므로, 출력해야 할 값은 55이다.



```python
number = int(input())
total=0

for i in range(1,number+1):
    total+=i

print(total)
```

