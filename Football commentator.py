def func(G1,P1,G2,P2,q):
  temp1 = G1 + G2
  temp2 = P1 + P2
  if temp1 > temp2:
    return 0
  elif temp1 == temp2:
    if q == 1 and P1 < G2:
      return 0
    elif q == 1 and P1 >= G2:
      return 1
    elif q == 2 and P2 < G1:
      return 0
    elif q == 2 and P2 >= G1:
      return 1
  elif temp1 < temp2:
    if q == 1 and P1 < G2 + temp2 - temp1:
      return temp2 - temp1 
    elif q == 1 and P1 >= G2 + temp2 - temp1:
      return temp2 - temp1 + 1
    elif q == 2 and P2 < G1:
      return temp2 - temp1 
    elif q == 2 and P2 >= G1:
      return temp2 - temp1 + 1
    
      
    
  
      
    
  

G1, P1 = map(int, input().split(":"))
G2, P2 = map(int, input().split(":"))
q = int(input())
print(func(G1,P1,G2,P2,q))
