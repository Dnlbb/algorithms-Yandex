n = int(input())
a = list()
for i in range(n):
  a.append(int(input()))

def func(n, a):
  cnt = 0
  for i in range(len(a)):
    while a[i] != 0:
      if a[i] // 4 != 0:
        temp = a[i] // 4
        a[i] -= 4 * temp
        cnt += temp
        continue
      elif a[i] % 4 == 3:
        cnt += 2
        break
      a[i] -= 1
      cnt += 1
  return cnt
        
print(func(n,a))
    
