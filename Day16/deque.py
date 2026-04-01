import collections

q=collections.deque([])

q.append(20)
q.append(30)
q.append(60)
q.append(70)
q.append(90)
q.popleft()
q.popleft()
q.popleft()
q.append(10)
q.append(40)

print(q) 