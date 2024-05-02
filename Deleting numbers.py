from collections import Counter
n = int(input())
xs = list(map(int, input().split()))
cnt = Counter(xs)
maxi = 0
for num in sorted(cnt):
    total = cnt[num] + cnt.get(num + 1, 0)
    maxi = max(maxi, total)
print(n - maxi)

