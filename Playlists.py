n, buf, k1 = int(input()), [], int(input())
vv = set(input().split())
rez = vv.intersection(vv)
for i in range(n-1):
    k = int(input())
    temp = set(input().split())
    rez = rez.intersection(temp)
print(len(rez))
print(" ".join(sorted(rez)))
