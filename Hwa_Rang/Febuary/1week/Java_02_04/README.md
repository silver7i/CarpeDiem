# TLI
1. 라이브 수업에서 핵심 개념 파악
2. 하루마다 올라오는 과제 3문제 바로 풀기 
3. 패턴 매칭에서 쓰이는 브루트포스, KMP 기억하기

# 코테 문제를 풀 때 조건문을 잘 작성하기
- 경우의 수를 충분히 생각할 것
- 참 조건이 안되면 거짓 조건을 생각할 것



# 배운내용
## 패턴 매칭(Pattern Matching)

문자열(또는 다른 자료)에서 특정 규칙(패턴)을 찾아내거나, 해당 패턴의 일치 여부를 검사하는 과정

- 사용자 입력이 형식에 맞게 작성하였는지 검사
- 데이터 추출등에 사용
- 정규표현식 사용 가능

## 브루트포스(Brute Force)

본문 문자열을 처음부터 끝까지 차례대로 순회하면서 패턴 내의 문자들을 전부 비교하는 방식으로 동작

최악의 경우 시간 복잡도는 텍스트의 모든 위치에서 패턴을 비교해야 하므로 O(MN)

## 브루트 포스 관련 문제

 - SWEA_1213_String
 -  SWEA_1216_회문2

## 회문
앞에서 부터 읽는 것과 뒤에서 부터 읽는 것이 동일한 문자열
회문 판별을 위해서는 문자열을 뒤집을 수 있어야함

문자열 뒤집는 법 
- for문을 사용해서 뒤집기
- StringBuffer or StringBuilder에서 reverse()사용
단 StringBuffer or StringBuilder는 메모리 사용을 주의해야 한다.

문자열은 불변이기 때문에 한 번 만들고 나면 중간에 수정을 할 수 없다.

## KMP(Knuth-Morris-Pratt) 알고리즘

패턴매칭 알고리즘 중에서 가장 빠름
최장 길이의 일치하는 접두사 ==  접미사 정보를 이용해 점프

LPS : Longest proper Prefix which is also a Suffix
 - proper: 자기 자신(전체)은 제외
 - ex) "level"
 	- prefix: l, le, lev, leve(o), level(x)
 	- suffix: l, el, vel, evel
 	-> LPS: "l"

