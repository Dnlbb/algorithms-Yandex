k = int(input())
xs = list()
for i in range(k):
  xs.append(list(map(int, input().split())))

def func(xs):
  minx = 10**10
  maxx = -1 
  miny = 10**10
  maxy = -1 
  for i in range(len(xs)):
    if xs[i][0] < minx:
      minx = xs[i][0]
    if xs[i][1] < miny:
      miny = xs[i][1]
    if xs[i][0] > maxx:
      maxx = xs[i][0]
    if xs[i][1] > maxy:
      maxy = xs[i][1]
  return minx,miny,maxx,maxy
a, v , c ,d = func(xs)
print(a,v,c,d)


