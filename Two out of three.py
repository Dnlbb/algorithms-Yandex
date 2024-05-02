n1 = int(input())
x1 = (set(list(map(int, input().split()))))
n2 = int(input())
x2 = (set(list(map(int, input().split()))))
n3 = int(input())
x3 = (set(list(map(int, input().split()))))
rez = []
rez.extend(x1.intersection(x2))
rez.extend(x2.intersection(x3))
rez.extend(x1.intersection(x3))
print(" ".join(map(str, sorted(set(rez)))))

