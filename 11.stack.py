import collections
stack = collections.deque()
print(stack)
stack.append(10)
stack.append(20)
stack.append(30)
stack.append(40)
print(stack)
stack.pop()
print(stack[-1])
if not stack:
  print('STACK Empty')

import queue
stack =  queue.LifoQueue() #LifoQueue(3)
stack.put(10)
stack.put(20)
stack.put(30)
stack.get() #pop
