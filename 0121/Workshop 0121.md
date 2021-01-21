# Workshop 0121

> python 04. 함수





## 1. 숫자의 의미



정수로 이루어진 list 를 전달 받아 , 각 정수에 대응되는 아스키 문자를 이어붙인 문자열을 반환하는 get_secret_word 함수를 작성하시오 . 단 , list 는 65 이상 90 이하 그리고 97 이상 122 이하의 정수로만 구성되어 있다.

```python
get_secret_word([83,115,65,102,89]) #=> 'SsAfY'
```

```python
def get_secret_word(cord):
    result = ''
    for i in cord:
        i = chr(i)
        result += i
    return result

 
answer = get_secret_word([83,115,65,102,89])   

print(answer)
```





## 2. 내 이름은 몇일까?

문자열을 전달 받아 해당 문자열의 각 문자에 대응되는 아스키 숫자들의 합을 반환하는 get_secret_number 함수를 작성하시오 . 단 , 문자열은 A~Z, a~z 로만 구성되어 있다.

```python
get_secret_number('tom') #=> 336
```

```python
def get_secret_number(name):
    result = 0
    for i in name:
        i = ord(i)
        result+=i
    return result

answer = get_secret_number('tom')
print(answer)
```





## 3. 강한 이름

문자열 2개를 전달 받아 두 문자열의 각 문자에 대응되는 아스키 숫자들의 합을 비교하여 더 큰 합을 가진 문자열을 반환하는 get_strong_word 함수를 작성하시오.

```python
get_strong_word('z','a') #=> 'z'
get_strong_word('tom', 'john') #=> 'john'
```

```python
def get_secret_number(name):
    result = 0
    for i in name:
        i = ord(i)
        result+=i
    return result

def get_strong_word(a,b):
    value_a = get_secret_number(a)
    value_b = get_secret_number(b)
    if value_a>value_b:
        return a
    else:
        return b

get_strong_word('z','a')
get_strong_word('tom', 'john')
```

