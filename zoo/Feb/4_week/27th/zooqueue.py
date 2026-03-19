# # 선형 큐
# def enqueue(item):
#     """
#     마지막 원소 뒤에 새로운 원소를 삽입하기 위해
#     rear 값을 하나 증가시켜 새로운 원소를 삽입할 자리를 지정
#     그 인덱스에 해당하는 배열원소 q[rear]에 item을 저장
#     """
#     global rear
#     if is_full():
#         print("Queue_Full")
#     else:
#         rear = rear + 1
#         q[rear] = item
#
#
# def dequeue():
#     """
#     가장 앞에 있는 원소를 삭제하기 위해
#     front 값을 하나 증가시켜 큐에 남아있는 첫 번째 원소로 이동
#     첫 번째 원소를 리턴 함으로써 삭제와 동일한 기능을 함
#     """
#     global front
#     if is_empty():
#         print("Queue_Empty")
#     else:
#         front = front + 1
#         return q[front]
#
#
# def is_empty():
#     """
#     공백상태: front == rear
#     """
#     return front == rear
#
#
# def is_full():
#     """
#     포화상태: rear == n-1 (n 배열의 크기, n-1 배열의 마지막 인덱스)
#     """
#     return rear == len(q) - 1
#
#
# def qpeek():
#     """
#     가장 앞에 있는 원소를 검색하여 반환하는 연산
#     현재 front의 한자리 뒤(front+1)에 있는 원소, 즉 큐의 첫 번째에 있는 원소를 반환.
#     """
#     if is_empty():
#         print("Queue_Empty")
#     else:
#         return q[front + 1]
#
#
# ## create_queue()
# """
# 크기 n인 1차원 배열 생성
# front와 rear를 -1로 초기화
# """
# n = int(input())
# q = [0] * n
# front = -1
# rear = -1
#
# ## 동작 확인
# """
# 세 개의 데이터 1, 2, 3을 차례로 큐에 삽입하고
# 큐에서 세 개의 데이터를 차례로 꺼내서 출력
# 1, 2, 3 이 출력되어야 함.
# """
# enqueue(1)
# enqueue(2)
# enqueue(3)
#
# print(dequeue())  # 1
# print(dequeue())  # 2
# print(dequeue())  # 3
#
# "================================================================================"
#
#
# # 원형 큐
# def enqueue(item):
#     """
#     마지막 원소 뒤에 새로운 원소를 삽입하기 위해
#     rear 값을 조정하여 새로운 원소를 삽입할 자리를 지정
#     그 인덱스에 해당하는 배열원소 cq[rear]에 item을 저장
#     """
#     global rear
#     if is_full():
#         print("Queue_Full")
#     else:
#         rear = (rear + 1) & len(cq)
#         cq[rear] = item
#
#
# def dequeue():
#     """
#     가장 앞에 있는 원소를 삭제하기 위해
#     front 값을 조정하여 삭제할 자리를 지정
#     새로운 front 원소를 리턴 함으로써 삭제와 동일한 기능을 함
#     """
#     global front
#     if is_empty():
#         print("Queue_Empty")
#     else:
#         front = (front + 1) % len(cq)
#         return cq[front]
#
#
# def is_empty():
#     """
#     공백상태 front == rear
#     """
#     return front == rear
#
#
# def is_full():
#     """
#     삽입할 rear의 다음 위치 == 현재 front
#     """
#     return (rear + 1) % len(cq) == front
#
#
# ## create_circle queue()
# """
# 크기 n인 1차원 배열 생성
# front와 rear를 0으로 초기화
# """
# cq = [0] * n
# front = rear = 0
#
# "================================================================================"
# # 연결 큐
# from collections import deque
#
# q = deque()
#
# q.append(1)  # enqueue() / 오른쪽에 1 추가
# t = q.popleft()  # dequeue() / 왼쪽에서 요소를 제거하고 반환, 요소가 없으면 IndexError
#
#
# class Node:
#     def __init__(self, item, n=None):
#         self.item = item
#         self.next = n
#
#
# def enqueue(item):  # 연결 큐의 삽입 연산
#     global front, rear
#     newNode = Node(item)  # 새로운 노드 생성
#     if front == None:  # 큐가 비어있다면
#         front = newNode
#     else:
#         rear.next = newNode
#     rear = newNode
#
#
# def is_empty():
#     return front == None
#
#
# def dequeue():  # 연결 큐의 삭제 연산
#     global front, rear
#     if is_empty():
#         print("Queue_Empty")
#         return None
#
#     item = front.item
#     front = front.next
#     if front == None:
#         rear = None
#     return item
#
#
# def qpeek():
#     return front.item
#
#
# def print_q():
#     f = front
#     s = ""
#     while f:
#         s += f.item + " "
#         f = f.next
#     return s
#
#
# front = None
# rear = None
# "================================================================================"
# from collections import deque
#
# q = deque()
# q.append(1)     # enqueue()
# t = q.popleft() # dequeue()
#
# list_q = []
# for i in range(1000000):
#     list_q.append(i)
# for _ in range(1000):
#     list_q.pop(0)
# print('end')
# # deque_q = deque()
# # for i in range(1000000):
# #     deque_q.append(i)
# # for _ in range(1000000):
# #     deque_q.popleft()
# # print('end')

from collections import deque
queue = deque()
total_candies = 1000000 # 나눠줘야 하는 총 캔디 수
given_candies = 0 # 나눠준 캔디 수
new_person = 1 # 새로운 사람의 번호표

last_person_id = 0 # 마지막으로 받아가는 사람 체크용

while given_candies < total_candies:
    queue.append((new_person, 1, 0)) # 새로운 사람 줄 서기

    # 맨 앞사람 처리 (curr_person_id : 막 받아간 사람, needs: 받아간 사탕, my_candies: 지금까지 내 사탕)
    curr_person_id, needs, my_candies = queue.popleft()

    given_candies += needs # 나눠준 캔디수 갱신
    last_person_id = curr_person_id

    # 다시 줄 서는 사람
    # (curr_person_id: 방금 받아간 사람, needs + 1 : 원래 요구하던 것보다 +1개 더, my_candies + needs: 지금까지 내사탕 방금 받은 것까지 포함해서 갱신)
    queue.append((curr_person_id, needs + 1, my_candies + needs))

    # new_person 추가
    new_person += 1

print(last_person_id)