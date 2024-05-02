N , K = map(int, input().split())
xs = list(map(int, input().split()))

def search12(xs,K):
  max = 0
  for i in range(len(xs)):
    if i - K >= 0:
      p = i - K
    elif i- K <0:
      p = 0
    for j in range(p, i):
      if xs[i] - xs[j] > max:
        max = xs[i] - xs[j]
  return max

print(search12(xs,K))
