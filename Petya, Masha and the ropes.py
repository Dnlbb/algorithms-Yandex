N = int(input())
xs = list(map(int, input().split()))

def func(xs):
  big = max(xs)
  index = xs.index(big)
  if big > sum(xs) - big:
    return (big * 2) - sum(xs)
  else: 
    return sum(xs)

print(func(xs)) 
