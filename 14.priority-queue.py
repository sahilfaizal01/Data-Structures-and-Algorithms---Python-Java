# using list
q = []
q.append(10)
q.append(30)
q.append(5)
q.append(40)
q.append(2)
q.sort()
q.pop(0)
q.pop(0)
print(q)

# using priority queue
import queue
q = queue.PriorityQueue()
q.put(10)
q.put(60)
q.put(40)
q.put(20)
print(q.get())
print(q.get())
