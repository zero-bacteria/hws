# Homework 0119 

데이터 & 제어문



## 1. mutable & immutable

제시 된 컨테이너들을 각각, 변경 가능한 것(mutable)과 변경 불가능한 것(immutable)으로 분류하시오.

아래에 답안을 작성하시오.



??? 주어진게 없음





## 2. 홀수 list

range와 slicing을 활용하여 1부터 50까지 숫자 중 홀수로 이루어진 리스트를 만드시오.

```python
a= list(range(1,51))

print(a[::2])
```



## 3. dictionary 생성

반 학생들의 정보를 이용하여 key는 이름, value는 나이인 dictionary를 만드시오.

```python
info = {'김영균':'27' , '임광훈': '26'}

```



## 4. 반복문으로 네모 출력

두 개의 정수 n과 m이 주어졌을 때, 가로의 길이가 n, 세로의 길이가 m인 직사각형 형태를 별(*) 문자를 이용하여 출력하시오. 단, 반복문을 사용하여 작성하시오.

```python
n = 5
m = 9


for i in range(1,m+1):
    print('*'*n)
```



## 5. 조건 표현식

제시된 if 문을 조건 표현식으로 바꾸어 작성하시오.

```python
temp = 36.5
if temp >= 37.5:
    print('입실 불가')
else:
    print('입실 가능')
```



```python
temp = 36.5

print('입실 불가') if temp>=37.5  else print('입실 가능')
```



## 6. list 평균값

제시된 list의 평균 값을 출력하시오.

```python
scores = [80, 89, 99, 83]

avg = sum(scores)/len(scores)

print(avg)
```

