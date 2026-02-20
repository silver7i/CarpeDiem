"""
10
"""

N = int(input())
num_arr = []

for i in range(1, N+1):
    to_str = str(i)
    hyphen = ''
    for j in to_str:
        if j in '369':
            hyphen += '-'
            i = hyphen
    num_arr.append(i)
         
print(*num_arr)