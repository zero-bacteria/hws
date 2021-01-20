# Workshop 0120



## 1. List 의 합 구하기

정수로만 이루어진 list 를 전달 받아 해당 list 의 모든 요소들의 합을 반환하는 list_sum 함수를 built in 함수인 sum() 함수를 사용하지 않고 작성하시오



```python
a= [1,2,3,4,5]

def list_sum(x):
    result = 0
    for i in x:
        result+=i
    return result

print(list_sum(a))
```

``` python
def list_sum(numbers):
    total = 0
    for number in numbers:
        total+= number
    return total

list_sum([1,2,3,4,5])
```



## 2. Dicionary로 이루어진 List의 합 구하기

Dictionary 로 이루어진 list 를 전달 받아 모든 dictionary 의 'age' key 에 해당하는 value 들의 합을 반환하는 dict_list_sum 함수를 built in 함수인 sum() 함수를 사용하지 않고 작성하시오



``` python
def dict_list_sum(students):
    total = 0
    for student in students:
        #student.get('age')
        total +=student['age']
    return total

a= dict_list_sum([
    {'name': 'kim', 'age' : 12},
    {'name':'lee', 'age':4}
    ])
print(a)
```



## 3. 2 차원 List 의 전체 합 구하기

정수로만 이루어진 2 차원 list 를 전달 받아 해당 list 의 모든 요소들의 합을 반환하는 all_list_sum 함수를 built in 함수인 sum() 함수를 사용하지 않고 작성하시오.



```python
def all_list_sum(number_lists):
    total = 0
    for number_list in number_lists:
        for number in number_list:
            total+=number
    return total

# 혹시 재귀함수로 가능한가 해보기 

a=all_list_sum([[1],[2,3],[4,5,6],[7,8,9,10]])

print(a)
```

