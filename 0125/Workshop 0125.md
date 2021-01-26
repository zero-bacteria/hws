# Workshop - 0125

> 데이터 구조 및 활용
>
> * 데이터구조
> * 메서드
> * 데이터구조의 특징에 대한 이해
> * 데이터 구조별 메서드 활용에 대한 이해





## 1. 평균 점수 구하기

key 값으로 과목명, value 값으로 점수를 가지는 dictionary를 전달받아, 전체 과목의 평균 점수를 반환하는 함수 get_dict_avg 함수를 작성하시오.

```python
get_dict_avg({
    'python' : 80,
    'algorighm' : 90,
    'django' : 89,
    'web' : 83,
}) #=>85.5
```

```python
def get_dict_avg(score_dict):
    score_list = []
    for key in score_dict:
        score_list.append(score_dict.get(key))
    
    result = sum(score_list)/len(score_list)

    return result

print(get_dict_avg({
    'python' : 80,
    'algorighm' : 90,
    'django' : 89,
    'web' : 83,
})) #=>85.5
```

```python
# 또다른 방법
result=[]
for score in scores.values():
	result.append(score)
	return result
```



## 2. 혈액형 분류하기

여러 사람의 혈액형(A, B, AB, O)에 대한 정보가 담긴 list를 전달 받아, key는 혈액형의 종류, value는 사람 수인 dictionary를 반환하는 count_blood 함수를 작성하시오.



```python
count_blood([
    'A', 'B', 'A', 'O', 'AB', 'AB',
'O', 'A','B','O','B','AB'
])#=> {'A':3, 'B':3, 'O':3, 'AB':3}

```



```python
def count_blood(blood_list):
    result = {}
    
    result['A']=blood_list.count('A')
    result['B']=blood_list.count('B')
    result['O']=blood_list.count('O')
    result['AB']=blood_list.count('AB')
    
    return result
 
print(count_blood([
    'A', 'B', 'A', 'O', 'AB', 'AB', 
    'O', 'A', 'B', 'O', 'B', 'AB'
    ]))#=> {'A':3, 'B':3, 'O':3, 'AB':3}
```

* 추가로 .get으로 지정하면 안되는 이유 알아보기 --> 됨, 아래와 같다

```python
def count_blood(blood_list):
    # 1. 결과값 변수 초기화
    blood_dict = {}
    
    # 2. blood_list 순회
    for blood in blood_list:
        # 혈액형 정보가 존재하면
        if blood_dict.get(blood):
            blood_dict[blood] +=1 # 1더하기
            #혈액형 정보가 없으면
            else:
                blood_dict[blood] = 1 # 1로 초기화
```

```python
# 더 간단히 하는 방식

for blood in blood_list:
    # 혈액형 정보가 존재하면 - > 0이 아님 -> 기존값+1
    # 혈액형 정보가 없으면  - > 0 -> 0+1 (1로 초기화)
    blood_dict[blood] = blood_dict.get(blood, 0) + 1
    
return blood_dict
```

* get 함수가 없으면 none 을 반환하는 것을 이용 추가로 none 대신 0을 반환하게 만드는 원리

  



