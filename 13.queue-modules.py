import collections
queue = collections.deque()
print(queue)
queue.appendleft(10)
queue.appendleft(20)
queue.appendleft(30)
queue.appendleft(40)
print(queue)
queue.pop()
print(queue[-1])
if not queue:
  print('Queue Empty')
