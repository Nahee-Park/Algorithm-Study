# 파이썬 기본 개념 정리

> 주의! 파이썬은 세미콜론; 붙이지 않는다!

## 자료형

### 수 자료형

1. 정수형

   ```python
   #양의 정수
   a= 1000
   #음의 정수
   b= -100
   ```

2. 실수형
   - 변수에 소수점 붙이면 실수형 변수로 처리
3. 지수 표현 방식

   - 임의의 큰 수를 표현할 때 이용
   
     ![Untitled](https://user-images.githubusercontent.com/81923229/122093300-e67dc700-ce45-11eb-9c23-a78696e3d575.png)
     
   - 최단 경로 알고리즘에서 도달할 수 없는 노드 ) INF (무한)으로 설정
   - 가능한 최댓값이 10억 미만이라면 1e9 사용
   - **주의) 실수형을 사용하면 딱 떨어지지 않는다**

     → round 함수 이용

     ```python
     # 123.456을 소수점 둘째자리까지만 남겨둠
     round(123.456,2)
     ```

4. 연산
   - `/` 연산자의 결과가 실수형 → 몫을 알고 싶다면 `// 연산자` 사용
   - `**` 거듭제곱 연산자
   - `%` 나머지 연산자 많이 쓰임
   - 기본적으로 연산자 많아서 굳이 라이브러리 필요 없음

### 리스트 자료형

1. 리스트 선언, 초기화

   ```python
   #리스트 선언 (두 가지 방법)
   a = []
   b = list()

   #리스트 초기화
   a = [1,2,3,4,5,6,7]

   #같은 원소로 채워진 리스트 만들기
   n=10
   a=[0]*n
   #[0,0,0,0,0,0,0,0,0,0,0]
   ```

2. 리스트 인덱싱

- 음수도 가능

  ```python
  a=[1,2,3,4,5,6,7]
  a[7] #6
  a[-1] #7
  ```

3. 리스트 슬라이싱

- 연속적인 위치를 갖는 원소들 가져올 때 사용
- 대괄호 안에 콜론을 넣어서 시작 인덱스, 끝 인덱스 설정
- 끝 인덱스는 실제 인덱스보다 1을 더 크게 설정

  ```python
  a=[1,2,3,4,5,6,7,8]

  #a[1]부터 a[3]까지
  a[1:4]
  ```

4. 리스트 컴프리헨션

- 대괄호 안에 조건문, 반복문 적용해서 리스트 초기화 → 매우 강력!

  ```python
  # 0~9까지의 범위 안의 i값을 돌면서 리스트 초기화
  a = [i for i in range(10)]
  print(a)
  #[0,1,2,3,4,5,6,7,8,9]
  ```

- 조건문도 포함 가능

  ```python
  #제곱수만 포함하는 리스트
  array = [(리스트에 출력할 것) for i in range(i의 시작범위,끝범위)(i에 관한 조건문)]

  array = [i * i for i in range(1,5)
  print(array) # [1,4,9,16,25]

  #0~9 안에서홀수만 포함하는 리스트
  array2 = [i for i in range(10) if i%2==1] #for문 안에 조건 더 들어갈 수 있음
  ```

- 2차원 리스트 초기화에 용이 ) **특히 2차원 리스트 한 번에 초기화 할 때 유용**

  ![Untitled 1](https://user-images.githubusercontent.com/81923229/122093360-f9909700-ce45-11eb-84ff-319f7941d09b.png)


  - 1차원 리스트의 초기화

    ```python
    #반복을 사용하되 그 변수를 직접적으로 사용하지 않으면 _로 나타냄
    #[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    array = [[0]*m for _ in range(20)]
    ```

  - 2차원 리스트의 초기화

    ```python
    # 가로 세로 N*M 크기의 2차원 리스트 초기화
    array = [[0]*m for _ in range(n)]

    # n = 4 , m = 3 이면
    # [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
    ```

- 관련 메소드

  ![Untitled 2](https://user-images.githubusercontent.com/81923229/122094138-c995c380-ce46-11eb-9bce-541a01661550.png)


  →remove()가 하나의 원소만을 삭제할 수 있기 때문에 여러 개 한번에 제거하려면 다른 처리 해줘야 함.

### 문자열, 튜플 자료형

1. 문자열

1. 구현

   - `/`쓰고 `"`쓰면 문자열 내부에서 "사용 가능

   ```python
   data = "Hello World" #Hello World
   data = "Don't you know /"Python/"?" #Don't you know "Python"?

   ```

1. 연산

   - 덧셈, 곱셈 가능
   - 그러나 특정 인덱스 수정 불가

1. 튜플

- 리스트와 유사
- 그러나 한 번 선언된 값 변경 불가, 소괄호 이용, 리스트에 비해 공간 효율적

  ```python
  a = (1,2,3,4,5,6,7,8,9)

  #네 번째 원소만 출력
  print(a[3])

  #두 번째부터 네 번째 원소까지 출력
  print(a[1:4])

  #실행 결과
  4 (2,3,4)
  ```

- **언제 사용?**
  1. 서로 다른 성질 데이터 묶어서 관리할 때
     - 최단 경로 알고리즘 (비용, 노드 번호)의 형태
  2. 데이터 나열을 hashing 키 값으로 사용할 때
     - 변경 불가능한 성질 이용
  3. 리스트보다 메모리를 효율적으로 써야할 때

### 사전, 집합 자료형

1. 사전 자료형

   - key, value의 쌍을 데이터로 가짐
   - key로 값을 찾을 수 있고, key는 변경불가능한 자료형으로만 사용 가능
   - 사전 자료형은 Hash Table을 이용해서 데이터 조회, 수정에 있어서 O(1)시간 안에 처리 가능

   ```python
   #약간 인덱스에 접근하는 느낌으로 초기화
   data = dict()
   data['사과']=98
   data['바나나']='banana'

   #객체 초기화하는 느낌으로 초기화
   data2 = {
   	'사과' : 98,
   	'바나나' : 'banana'
   }

   #data와 data2 둘 다 결과 값이 같음

   list(data.keys()) #key값만 리스트 형태로 출력
   data.values() #value값만 출력, 그러나 리스트 형변환 안해줘서 객체 형태로 출력됨
   ```

2. 집합 자료형

   1. 구현

      - 리스트나 문자열을 이용해 초기화
      - 중복 허용 X, 순서 없음

      ```python
      data = {1,2,3,4,4,5}
      data2 = set([1,2,3,4,4,5])
      #두 값이 같음
      #{1,2,3,4,5}
      ```

   2. 연산

      - 합집합, 교집합, 차집합 이용 가능

      ```python
      a = {1,2,3,4,5}
      b = {3,4,5,6,7}

      #합집합
      a|b
      #교집합
      a&b
      #차집합
      a-b
      ```

   3. 자주 쓰이는 함수

      ```python
      data={1,2,3}

      #새로운 원소 추가
      data.add(5)

      #새로운 원소 여러개 추가
      data.update([5,6,7])

      #특정 원소 삭제
      data.remove(3)
      ```

   **사전, 집합 자료형 언제 사용?**

   - 리스트와 튜플은 인덱싱 이용해 값 얻음
   - 사전 자료형은 key로, 집합 자료형은 원소 그 자체로 접근 → O(1)의 시간복잡도록 조회

## 기본 입출력

### 입력

1. 일반적 입력

   ```python
   #int형으로 인풋 받고 a활용 가능
   a = int(input())

   #input값을로 받은 것을 공백 기준으로 나누어 int형으로 바꾼다음 list로 사용
   #그럼 data는 입력받은 값들의 리스트임!!! 정말 많이 쓰임
   data=list(map.(int,input().split()))

   #세 개의 값만 받는다면 이것도 가능
   #구조분해할당같은 느낌인데 조금 다른 것은 딱 변수 갯수에 맞추지 않으면 오류뜸!
   a, b, c = map.(int,input().split())
   ```

2. 빠르게 입력

- 이진탐색, 정렬, 그래프 관련 문제에서 입력 때문에 시간 초과되기도 해서 이용

  ```python
  import sys

  #.rstrip()까지 사용해야 엔터가 줄바꿈기호로 입력되지 않음
  data = sys.stdin.readline().rstrip()
  ```

### 출력

- 기본적으로 print() 사용, 여기엔 줄바꿈 기호가 내제되어있음

  ```python
  #줄바꿈 원치 않으면 end="" 추가해서 줄바꿈 대신 공백이 있도록

  print(7, end="")
  print(8, end="")
  # 출력결과 7 8

  a = 3

  #f-string을 통해 변수 출력 가능
  print(f"정답은{a} 입니다!")
  ```

## 조건문

1. if- elif문

   - 파이썬은 코드 블록을 들여쓰기로 지정 → 공식 가이드 라인에선 스페이스바 4개로

     ![Untitled 3](https://user-images.githubusercontent.com/81923229/122093429-09a87680-ce46-11eb-8a32-61d252d6f755.png)


   - 조건문 간소화

     - 조건문 표현식에서는 `if조건문`을 만족시킬 때 시행시킬 구문을 `if조건문` 왼쪽에 작성하고, `else` 뒤에 실행될 구문을 오른쪽에 작성한다

     ![Untitled 4](https://user-images.githubusercontent.com/81923229/122093506-188f2900-ce46-11eb-9d69-2e0bb0f184b0.png)

2. 논리 연산자

   - &&, ||, !가 아니라 직접 말로 쓴다

     ![Untitled 5](https://user-images.githubusercontent.com/81923229/122093529-1dec7380-ce46-11eb-9c4f-fc0278bfb5a9.png)


3. in, not in 연산자

   - [], {} , (), "" 모두에서 사용 가능 (리스트, 딕셔너리, 튜플, 문자열 전부)

     ![Untitled 6](https://user-images.githubusercontent.com/81923229/122093551-22b12780-ce46-11eb-9ca1-7920c984f26b.png)


4. pass 키워드

   - 그 조건문 아무것도 안하고 그냥 조건문 밖으로 넘어감.

   ![Untitled 7](https://user-images.githubusercontent.com/81923229/122093572-2775db80-ce46-11eb-8ff6-03540d2db0dc.png)

## 반복문

**while문보다 for문이 대체로 더 간결한 경우 많음!**

1. while문

   ![Untitled 8](https://user-images.githubusercontent.com/81923229/122093585-2c3a8f80-ce46-11eb-87d6-83bdf36a7970.png)


   ```python
   while 조건문:
   	실행시킬 값
   	break #빠져나가고 싶을 때 사용

   #i가 5일 때 반복문 나감
   i=1
   while true:
   	print("현재 i의 값",i)
   	if i==5:
   		break
   	i += 1

   ```

2. for문

   - 특정 데이터의 원소 첫번째 인덱스 부터 방문

     ![Untitled 9](https://user-images.githubusercontent.com/81923229/122093618-352b6100-ce46-11eb-89a8-a88dc084746d.png)


     ```python
     array = (1,2,3)
     for x in array:
     	print(x)
     ```

   - 그냥 연속적인 값을 순회 : `range(시작값, 끝값+1)` 사용

     ```python
     result = 0

     #1부터 9까지의 값을 순회
     for i in range(1,10):
     	result += i
     print(result)
     ```

   - continue 키워드 : 남은 코드 실행 안하고 다음 반복을 진행하고자 함

     ```python
     result = 0

     for i in range(1,10):
     	if i % 2 == 0:
     		continue #짝수는 뒤의 코드 실행 안하고 다시 반복문의 처음으로 감
     	result += i

     #1부터 9까지 홀수의 합을 구할 수 있음
     ```

## 함수의 람다 표현식

1. 기본적인 함수 표현식

   ```python
   def 함수명(받을 파라미터):
   	해당 함수에서 수행할 일

   def substract(a,b):
   	return a-b

   print(substract(b=3,a=10) #이런 식으로 변수 직접 지정 가능
   ```

   <특징>

   - 변수 직접 대입 가능
   - 리턴 여러 개 한번에 할 수 있음
   - 전역 변수를 함수 내부에서 쓰기 위해서는 global 키워드 사용해야됨

     ```python
     a = 3
     def func():
     	global a += 3 # 이거 안해주면 내부에 정의된 a가 없으므로 오류메시지 뜸
     	return a
     ```

   - 그러나 참조는 그냥 전역변수 사용할 수 있음

     특히 리스트는 전역으로 많이 쓰여서 이런 식의 연산 많음

     ```python
     array = [1,2,3,4,5]

     def func():
     	array.append(6)

     func()
     print(array)
     #[1,2,3,4,5,6]
     ```

2. 람다 표현식

   - 익명 함수의 느낌, 특정 기능을 수행하는 함수를 한 줄에 작성 가능함

     `(lambda 받을 인자:수행할 일)(실제로 넣을 인자)`

     ```python
     #일반적인 함수 활용법
     def add(a,b):
     	return a+b;
     print(add(3,4))

     #람다 표현식을 이용
     print((lambda a,b:a+b)(3,4))
     ```

   - 내장 함수에서 자주 쓰임

     ```python
     #sorted(정렬할 배열, key=어떠한 함수(정렬기준이 명시된))

     array=[('나히',22),('민지',19),('엄마',49)]

     #어떤 튜플이 원소로 주어졌을 때 그 두번째 원소를 리턴 -> 그 함수를 기준으로 하도록 key속성에 넣음
     def my_key(x):
     	retrun x[1]

     print(sorted(array, key=my_key))
     print(sorted(array, key=lambda x:x[1]))
     ```

   - 여러 개의 리스트에 동일한 함수를 적용하고자 할 때

     ```python
     #map(적용하고자 하는 함수,적용할 데이터(리스트, 튜플 등))

     list1=[1,2,3,4,5]
     list2=[6,7,8,9,10]

     result = list(map(lambda a,b=a+b, list1, list2))

     print(result)
     #[7,9,11,13,15]
     ```

## 자주 사용되는 표준 라이브러리

1. 유용한 표준 라이브러리
   - 내장함수
   - itertools: 반복되는 형태 데이터를 처리 ) 순열, 조합 라이브러리 코테에서 자주 사용
   - heapq: 힙 자료구조 제공 → 우선 순위 큐 기능 구현하기 위해
   - bisect: 이진탐색 기능 제공
   - collections: 덱, 카운터 등 자료구조 포함
   - math: 필수적인 수학적 기능을 제공 ) 팩토리얼, 제곱근, 최대 공약수, 삼각함수, 파이같은 상수 포함
2. 유용한 내장함수

   - 기본 내장함수

     ```python
        # sum() 합
        result_sum = sum([2, 3, 4, 5, 6])
        print(result_sum)

        # min() max() 최소 최대
        result_min = min(3, 5, 1, 2, 6)
        result_max = max(3, 5, 1, 2, 6)
        print(result_min)
        print(result_max)

        # eval() 실제 계산 결과
        print(eval("(2+3)*4"))

        # sorted 오름차순
        print(sorted([1, 2, 3, 9, 8, 7, 6]))
        print(sorted([1, 2, 3, 9, 8, 7, 6], reverse=True))

        # sorted() with key
        array = [('나히', 22), ('민지', 19), ('엄마', 49)]
        print(sorted(array, key=lambda x: x[1]))
     ```

   - itertools 라이브러리 내부의 순열 조합

     > 모든 경우의 수를 계산을 해서 해당 문제를 풀 때 모든 경우의 수를 구하는 방식이 통할지 안통할지를 짐작하는 방식으로 많이 사용  
     > 순열값이 막 천만을 넘어가면 완전탐색 시간초과될 확률이 크므로. 이런 식으로 순열 조합 이용해 문제 풀이 방향 설정

     1. 순열

        ```python
        from itertools import permutations

        data=['A','B','C'] #데이터 준비
        result = list(permutations(data,3)) #모든 순열 구하기
        print(result)
        ```

        ![Untitled 10](https://user-images.githubusercontent.com/81923229/122093632-3b214200-ce46-11eb-92fd-6206a104554c.png)


     2. 조합

        ```python
        from itertools import combinations

        data=['a','b','c']
        result = list(combinations(data,2)) #2개 뽑는 모든 조합 구하기
        ```

     3. 중복 순열과 중복 조합

        ```python
        #중복 순열
        from itertools import product
        data=['a','b','c']

        result=list(product(data,repeat=2)) #2 개를 뽑는 모든 순열 구하기(중복 허용)

        #중복 조합
        from itertools import combinations_with_replacement
        data=['a','b','c']

        result=list(combinations_with_replacement(data,2)) #2개를 뽑는 모든 조합 구하기 (중복 허용)
        ```

   - collections 라이브러리의 Counter 함수

     ```python
     from collections import Counter

     counter = Counter(['red','blue','blue','red','red','green'])

     print(counter['blue']) #blue 등장 횟수
     print(dict(counter)) #사전 자료형으로 반환

     #실행결과
     2
     {'red':3,'blue':2,'green':1}
     ```

   - math 라이브러리의 최대공약수, 최소공배수

     ```python
     import math

     #최대공약수
     math.gcd(21,14)

     #최소공배수
     math.lcm(21,14)
     ```
