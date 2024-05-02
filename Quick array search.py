N = int(input())
xs = list(map(int, input().split()))
k = int(input())
mas = []
for i in range(k):
    mas.append(list(map(int, input().split())))
xs.sort()
def bin_search(arr, x1, x2):
    left, right = 0, len(arr) - 1
    left1, right1 = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < x1:
            left = mid + 1
        else:
            right = mid - 1
    while left1 <= right1:
        mid1 = (left1 + right1) // 2
        if arr[mid1] <= x2:
            left1 = mid1 + 1
        else:
            right1 = mid1 - 1
    return left, left1

rez = []
for i in range(k):
    left_index, right_index = bin_search(xs, mas[i][0], mas[i][1])
    rez.append(right_index - left_index)

print(" ".join(map(str, rez)))
