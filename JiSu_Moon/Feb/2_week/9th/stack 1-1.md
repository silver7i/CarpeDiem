# TIL
1. 라이브 수업 복습
2. SWEA 2문제 풀기

---
## 오늘의 수업 : SW 문제 해결 기본 : Stack 1-1
---
## 스택(Stack)
물건을 쌓아 올리듯 자료를 쌓아 올린 형태의 자료구조
### 스택의 특성 : 후입선출(LIFO)
### 스택의 연산
- 삽입 (Push) : 저장소에 자료를 저장하는 연산
- 삭제 (Pop) : 저장소에서 삽입한 자료의 역순으로 꺼내는 연산
- 스택이 공백인지 아닌지를 확인하는 연산 (isEmpty)
- 스택의 top에 있는 item(원소)를 반환하는 연산 (peek) : 삭제 X

```
# 간단한 스택
top = -1
stack = [0] * 10

top += 1            # push(1)
stack[top] = 1
top += 1            # push(2)
stack[top] = 2
top += 1            # push(3)
stack[top] = 3

top -= 1            # pop()
print(stack[top+1])
top -= 1            # pop()
print(stack[top+1])
top -= 1            # pop()
print(stack[top+1])
```
```
st = []
st.append(1)
st.append(2)
st.append(3)
print(st.pop())
print(st.pop())
print(st.pop())
```

---
### 괄호검사
```
'''
( )( )((( )))
((( )((((( )( )((( )( ))((( ))))))
())
(()
)(
'''
txt = input()

top = -1
stack = [0] * 100

ans = 1
for x in txt:
    if x == '(':    # 여는 괄호 push
        top += 1
        stack[top] = x
    elif x == ')':  # 닫는 괄호인 경우
        if top == -1:   # 스택이 비어있으면 (여는 괄호가 없으면 )
            ans = 0
            break   # for x
        else:           # 여는 괄호 하나 버림
            top -= 1    # pop
if top != -1:   # 여는 괄호가 남아있으면
    ans = 0

print(ans)
```

---
### Function Call
프로그램에서의 함수 호출과 복귀에 따른 수행 순서를 관리
가장 마지막에 호출된 함수가 가장 먼저 실행을 완료하고 복귀하는 후입선출 구조