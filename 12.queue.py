queue = []
n = 5
def enqueue():
  if(len(queue)==n):
    print('Queue full')
  else:
    ele = input('Enter the element')
    queue.append(ele)
    print(queue)

def dequeue():
  if not queue:
    print('Queue empty')
  else:
    queue.pop(0)
    print(queue)

def display():
  print('Rear Element is ',queue[-1])
  print('Front Element is ',queue[0])
  print('Stack display',stack)

while True:
  print('Select queue operations: 1)add 2)remove 3)show 4)quit')
  choice = int(input())
  if choice == 1:
    enqueue()
  elif choice == 2:
    dequeue()
  elif choice == 3:
    display()
  elif choice == 4:
    break
  else:
    print('Enter correct choice')
