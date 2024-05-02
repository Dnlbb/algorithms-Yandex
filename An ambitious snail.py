N = int(input())  
berries = []

for i in range(N):
    a, b = map(int, input().split())  
    berries.append((a, b, i + 1))  


positive_diff_berries = [(a, b, index) for a, b, index in berries if a - b > 0]
negative_diff_berries = [(a, b, index) for a, b, index in berries if a - b <= 0]


positive_diff_berries.sort(key=lambda x: x[1]) 
negative_diff_berries.sort(key=lambda x: x[0], reverse=True) 


sorted_berries = positive_diff_berries + negative_diff_berries

max_height = 0
current_height = 0
order = []


for a, b, index in sorted_berries:
    current_height += a
    max_height = max(max_height, current_height)
    current_height -= b
    order.append(index)


print(max_height)
print(' '.join(map(str, order)))


