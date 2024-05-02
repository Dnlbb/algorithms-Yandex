def min_segments(t, test_cases):
    results = []
    for n , arr in test_cases:
        lengths = []
        count = 1
        MinEl = arr[0]
        for i in range(1, len(arr)):
            MinEl = min(MinEl, arr[i])
            if MinEl < count + 1:
                lengths.append(count)
                count = 0
                MinEl = arr[i]
            count += 1
        if count != 0:
            lengths.append(count)
        results.append((len(lengths),lengths))
    return results
def read_input():
    t = int(input())
    test_cases = []
    for _ in range(t):
        n = int(input())
        arr =list(map(int, input().split()))
        #print(arr)
        test_cases.append((n, arr))
    return t, test_cases
t, test_cases = read_input()
rez = min_segments(t, test_cases)
for otv in rez:
    print(otv[0])
    print(' '.join(map(str, otv[1])))
