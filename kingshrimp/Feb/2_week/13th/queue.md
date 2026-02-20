# 큐에 대해서

오늘은 큐에대해서 배웠다.
큐는 선입선출을 하는것이 원리이다. FIFO(First in First out)

큐를 사용하는 방법

```py
from collections import deque

queue = deque([1, 2, 3])
queue.append(4)
print(queue.popleft())
```

큐에다가 넣는것은 엔큐라고 하고
큐에서 값을 빼내는것은 디큐라고 한다.

