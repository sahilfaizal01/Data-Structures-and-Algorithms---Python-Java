stack = []
n = 10

def push():
  if len(stack) == n:
    print('Stack is full')
  else:
    ele = input('Enter the element:')
    stack.append(ele)
    print(stack)

def pop_element():
  if not stack:
    print('Stack is Empty')
  else:
    e = stack.pop()
    print('Removed Element is ',e)
    print(stack)

while True:
  print('SELECT THE Operation: 1) Push 2)Pop 3)Top/Peek 4)Exit')
  choice = int(input())
  if choice==1:
    push()
  elif choice==2:
    pop_element()
  elif choice==3:
    print('Top element is ',stack[-1])
  elif choice==4:
    break
  else:
    print('ENTER the correct option')
