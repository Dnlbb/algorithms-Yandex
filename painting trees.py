def func(p, v, q, m):
  maxp = max(p + v, q + m)
  re1 = maxp - max(p , q)
  minp = min(p - v, q - m)
  re2 = min(p , q) - minp
  if abs(p - q) <= m + v:
    re3 = abs(p - q) + 1
  elif abs(p - q) > m + v:
    re3 = m + v + 2
  return re1 + re2 + re3 
      
  
p, v = map(int, input().split())
q, m = map(int, input().split())
print(func(p, v, q, m))
