# Homework 0429

> JavaScript 기초



* JavaScript





## 문제 1.

아래의 설명을 읽고 T/F 여부를 작성하시오.



let & const 키워드로 선언한 변수와 var 키워드로 선언한 변수의 유일한 차이점은 변수의 유효범위이다.

```
F / 차이점 1. 블록, 2. 변수재선언
```

"값이 없음"을 표현하는 값으로 null 과 undefined 두 종류가 있으며 둘 다 typeof 연산자에서undefined 가 반환된다.

```
F / null은 object, undefined는 그냥 undefined
```

for in 문을 통해 배열의 각 요소를 순회할 수 있다

```
F / 각 요소를 순회하는 것이 아닌 인덱스가 나올것 이다.
```

`==`연산자는 두 변수의 값과 타입이 같은지 비교하고 같다면 true 아니면 false 를 반환한다.

```
F / 타입을 같게 만든 후에 비교한다.
```

JavaScript 에서 함수는 변수에 할당 , 인자로 전달할 수 있으나 함수의 결과값으로 반환할 수는 없다.

```
F / 반환할 수 있음 - 일급객체
```





## 문제 2.

다음의 Array Helper Method의 동작을 간략히 서술하시오.

map, filter, find, every, some, reduce

예) forEach 배열의 요소를 하나씩 순회한다.



map : 요소를 돌면서 각 요소에다가 callback을 실행시키고 결과를 다른 리스트를 만들어줌

filter : 요소중에 callback 함수를 만족하는 요소만으로 만듬

find : callback 함수를 만족하는 첫번째 요소를 찾음

every: 조건에 모두 통과되면 true 한개라도 통과 못하면 false

some: 하나의 조건이라도 통과하면 true 하나도 통과 못하면 false

reduce: acc callback 함수를 통과한 다음 하나의 값으로 하는 배열의 합?





## 문제 3.

아래의 숫자 배열에 map 함수를 사용하여, 모든 아이템에 3제곱을 한 새로운 배열을 만드는 코드를 작성하시오.

```js
const nums = [1, 2, 3, 4]
```



```js
const cubedNums = nums.map((num) => {
    return num ** 3
})
```

