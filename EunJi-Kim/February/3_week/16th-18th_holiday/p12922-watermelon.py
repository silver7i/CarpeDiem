'''
정수 n
'''


def solution(n):
    answer = ''
    
    for i in range(n):
        if i % 2 == 0: # 홀수 인덱스 이면
            answer += '수'
        else:
            answer += '박'
    
    return answer