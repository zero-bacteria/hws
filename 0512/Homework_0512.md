

# Homework 0512

> Vuex





## 문제 1.

아래의 설명을 일고 T/F 여부를 작성하시오.


Vue 프로젝트에서 상태 관리를 하기 위해서는 반드시 Vuex 를 설치해야 한다.

```
F
```

mutation 은 반드시 state 를 수정하기 위해서만 사용되어야 한다.

```
T
```

mutation 은 store.dispatch 로 action 은 store.commit 으로 호출할 수 있다.

```
F
```

state 는 data 와 동일하고 getters 는 computed 와 동일한 동작을 한다.

```
T
```







## 문제 2.

Vuex에서 action과 mutation의 역할과, 두 함수의 차이를 서술하시오.



mutation은 동기적인 작업, 데이터를 변경하는 일을 함

action에서는 비즈니스 로직, 대부분의 작업, 비동기도 가능