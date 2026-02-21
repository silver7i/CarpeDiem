# TIL
1. SWEA 5문제 풀기

---
## 오늘의 수업 : SW 문제 해결 기본 : Stack 2-1
---
## 후위표기법
중위 표기법 : 연산자를 피연산자의 가운데 표기하는 방법
후위 표기법 : 연산자를 피연산자 뒤에 표기하는 방법

Step1. 중위 표기법의 후위 표기법 변환 방법
```
'''
(6+5*(2-8)/2)
6528-*2/+
'''

stack = [0] * 10
top = -1

icp = {'(':3, '*':2, '/':2, '+':1, '-':1}   # 밖에 있을때의 우선 순위 (클수록 높음)
isp = {'(':0, '*':2, '/':2, '+':1, '-':1}   # 스택안에서의 우선 순위 ( " )

infix = '(6+5*(2-8)/2)'
postfix = ''

for token in infix:
    if token not in '(+-*/)':   # 피연산자면 후위식에 추가
        postfix += token
    elif token == ')':          # 여는 괄호를 만날 때까지 pop
        while top>-1 and stack[top] != '(':
            top -= 1
            postfix += stack[top+1]
        if top != -1:   # 전체 수식이 괄호로 둘러 쌓이지 않은경우 대비
            top -= 1    # '(' 버림...
    else:                      # 연산자인 경우
        if top == -1 or isp[stack[top]] < icp[token]:  # 토큰의 우선순위가 더 높으면
            top += 1  # push
            stack[top] = token
        elif isp[stack[top]] >= icp[token]: # 토큰과 같거나 더 높으면
            while top > -1 and isp[stack[top]] >= icp[token]:
                postfix += stack[top]
                top -= 1
            top += 1  # push
            stack[top] = token
    print(postfix, stack, top)  # 처리 단계별로 상태 출력
while top > -1:                 # 바깥 괄호가 없는 경우 '6+5*(2-8)/2'
    top -= 1                    # 스택의 모든 연산자 pop
    postfix += stack[top + 1]
print(postfix)
```

Step2. 후위 표기법 식을 Stack을 이용하여 계산
```
#susik = '6528-*2/+'
for x in susik:
    if x not in '+-/*': # 피연산자면...
        top += 1            # push(x)
        stack[top] = int(x)
    else:
        op2 = stack[top]  # pop()
        top -= 1
        op1 = stack[top]  # pop()
        top -= 1
        if x=='+':  # op1 + op2
            top += 1                # push()
            stack[top] = op1 + op2
        elif x=='-':
            top += 1
            stack[top] = op1 - op2
        elif x=='/':
            top += 1
            stack[top] = op1 / op2
        elif x=='*':
            top += 1
            stack[top] = op1 * op2

print(stack[top])
```

---
## Backtracking
후보해를 구성해 나가다가, 더이상 해가 될 수 없다고 판단되면 되돌아가서(backtrack) 다른 후보를 찾는 방법
- 모든 경우의 수를 탐색하는 완전 탐색을 효율적으로 구현하는 방법
- 가능성이 있는 해를 추가해가며 완전한 해인지 검사
- 추가한 해가 가능성이 없는 경우 다른 해를 추가할 수 있는 이전 상태로 되돌아 가서 계속 탐색
- 최적화 문제와 결정 문제에 적용 (N-Queen 문제, 미로 찾기, 순열/조합, 부분집합, 스도쿠)