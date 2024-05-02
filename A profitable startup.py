def extend_profit(n, d, k):
    n_str = str(n)
    remainder = n % k

    for day in range(d):
        found = False
        for digit in range(10): 
            new_remainder = (remainder * 10 + digit) % k
            if new_remainder == 0:  
                n_str += str(digit)  
                remainder = new_remainder  
                found = True
                break  
        if not found:  
            return -1 

    return n_str  

n, k, d = map(int, input().split())
print(extend_profit(n, d, k))
