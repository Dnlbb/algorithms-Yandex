str1, str2 = input(),input()
xs = sorted(list(str1))
ys = sorted(list(str2))
if len(xs) != len(ys):
    print('NO')
else:
    for i in range(len(xs)):
        if xs[i] != ys[i]:
            print('NO')
            break
    else:
        print('YES')
