n, k = map(int, input().split())
xs = list(map(int, input().split()))

uni = set()
rep = False

for i, x in enumerate(xs):
    if x in uni:
        print('YES')
        rep = True
        break
    uni.add(x)
    if i >= k:
        uni.remove(xs[i - k])
if not rep:
    print('NO')

