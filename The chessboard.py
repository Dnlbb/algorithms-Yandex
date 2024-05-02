N = int(input())
xs = list()
for _ in range(N):
  xs.append(list(map(int, input().split())))

def func(xs,N):
  dx = (-1,0,1,0)
  dy = (0,1,0,-1)
  ans = 0
  for i in range(N):
    temp = 4
    for k in range(4):
      if [xs[i][0] + dx[k], xs[i][1] + dy[k]] in xs:
        temp -= 1
    ans += temp
  return ans

print(func(xs,N))
