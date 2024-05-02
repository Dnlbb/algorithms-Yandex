n = int(input())
xs = list(map(int, input().split()))
a , b , k = map(int, input().split())

def func(a, b, k, xs, n):
    max_right = -10 ** 10
    max_left = -10 ** 10
    if a % k == 0:
        left_gr = ((a - 1) // k)
    else:
        left_gr = (a // k)
    if b % k == 0:
        right_gr = ((b - 1) // k)
    else:
        right_gr = (b // k)
    ys = xs[::-1]
    holder = xs[0]
    ys.insert(0,holder)
    ys.pop()
    if a == b:
        return max(xs[left_gr % n],ys[left_gr % n])
    if (b-a) // k >= n:
        return max(xs)
    else:
        for i in range(left_gr,right_gr + 1):
            if max_right < xs[i % n]:
                max_right = xs[i % n]
            if max_left < xs[(i * -1) % n]:
                max_left = xs[(i * -1) % n]
        return max(max_right,max_left)
print(func(a,b,k,xs,n))
