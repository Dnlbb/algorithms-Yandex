signs = list()

def helper(numbers):
  for i in range(2,len(numbers)):
    if numbers[i] % 2 == 0:
      signs.append('+')
    elif numbers[i] % 2 == 1:
      signs.append('+')
      return i + 1
      

def func(numbers):
  cnt = 0 
  if (numbers[0] % 2 == 0 and numbers[1] % 2 == 1):
    signs.append('+')
    cnt = 2
  elif (numbers[0] % 2 == 1 and numbers[1] % 2 == 0):
    signs.append('+')
    cnt = 2
  elif numbers[0] % 2 == 1 and numbers[1] % 2 == 1:
    signs.append('*')
    cnt = 2
  elif numbers[0] % 2 == 0 and numbers[1] % 2 == 0:
    signs.append('+')
    cnt = helper(numbers)
  for i in range(cnt, len(numbers)):
    if numbers[i] % 2 == 0:
      signs.append('+')
    else:
      signs.append('*')
  
    
n = int(input())
numbers = (list(map(int, input().split())))
func(numbers)
mod = ['x' if element == '*' else element for element in signs]
s = ''.join(mod)
print(s)

