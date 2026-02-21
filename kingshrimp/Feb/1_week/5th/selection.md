# 선택정렬

선택정렬이란 가장 작은 값을 찾아서 이 값을 맨 앞에 두는 정렬이다.

문번:
```py
for i in range(len(arrary)):
    min_index = i
    for j in range(i+1, len(array)):
        if arr[min_index] > array[j]:
            min_index = j

    array[i], array[min_index] = array[min_index], array[i]
print(array)
```

이 내용을 공부를 하면서 얻어가야할 부분은 무엇인가?
이중반복문을 쓸 때 현재위치를 i로 하고 그 아래 반복문을 i+1부터 도는 것이다. 
바깥 반복문의 변수의 위치와 관련됭어서 안의 반복문을 결정을 할 때 유용해보인다.
for문을 쓸때 범위에 len을 넣으면 해당하는 인덱스 값을 구할 수 있다.
두개의 값을 서로 변경을 할 때 ,  = , 이런식을 이용을 해서 변경을 한다.
이외에는 다 알고 있는 사실이다.
