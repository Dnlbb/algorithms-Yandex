from re import L
def find_min_time(L_A, L_B, v_A, v_B, C):
    if L_A < 0:
      L_A = C + L_A
    if L_B < 0:
      L_B = C + L_B
    theta_A0 = (L_A / C) * 2 * 3.141592653589793
    theta_B0 = (L_B / C) * 2 * 3.141592653589793
    omega_A = (2 * 3.141592653589793 * v_A) / C
    omega_B = (2 * 3.141592653589793 * v_B) / C
    min_time = float('inf')
    if v_A == v_B == 0 and not(L_A + L_B == C or L_A == L_B):
      return "NO"
    elif v_A == v_B == 0 and (L_A + L_B == C or L_A == L_B):
      return "YES", 0
    if L_A == L_B:
      return "YES", 0
    if v_A == v_B and L_A != L_B:
      if v_A>0:
        return "YES", (2 * C - L_A - L_B) % C / (v_A + v_B)

      elif v_A<0:
        return "YES", ((abs(L_A) + abs(L_B)) / (2 * abs(v_A)))
    

    if v_A < 0 and v_B < 0:
      min_time = -((L_A + L_B - (2*C)) % C)  / (v_A + v_B)
      return "YES", min_time
    if v_A == 0 and v_B < 0:
      min_time = -((L_A + L_B - (2*C)) % C)  / (v_A + v_B)
      return "YES", min_time
    if v_B == 0 and v_A < 0:
      min_time = -((L_A + L_B - (2*C)) % C)  / (v_A + v_B)
      return "YES", min_time
      
