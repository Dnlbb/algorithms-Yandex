def minimum(x, y, p):
    def N(x, y, p):
        Colvo = 0
        for _ in range(10000):
            Colvo += 1
            p -= x - y
            x -= p
            y = 0
            if x <= 0:
                return False, Colvo
            if p <= 0:
                return True, Colvo
    d = {}
    hp = y
    while hp >= 0:
        to_dest = 0
        enem_s = p
        my_s = x
        b_hp = hp
        if my_s > 0 and b_hp > 0:
            if my_s - b_hp >= enem_s:
                d[hp] = 1
                hp -= 1
                continue
        if my_s > b_hp:
            isPoss, to_dest = N(my_s, b_hp, enem_s)
            if isPoss:
                d[hp] =to_dest
                hp -= 1
                continue
        hp -= 1
    return d


def help_F(x,y,p):
  cnt_r, opps, ever = 0 , 0 , minimum(x, y, p)
  rounds = []
  while x > 0 and y > 0:
    if cnt_r == 0:
        if x >= y:
            print(1)
            exit()
        else:
            y -= x
        cnt_r += 1
        cur =minimum(x, y, p).get(y, -1) + cnt_r if y in ever else -1
        if cur != -1:
            rounds.append(cur)
        continue
    cnt_r += 1
    if y > 0:
        opps += p
    if x > opps and y > 0:
        y -= x - opps
        opps = 0
        cur = minimum(x, y, p).get(y, -1) + cnt_r if y in ever else -1
        if cur != -1:
            rounds.append(cur)
    if x <= opps and y > 0:
        if x >= y:
            opps -= x - y
            y = 0
            x -= opps
    if x < opps and y < 0:
        break
    if y <= 0 and opps <= 0:
        rounds.append(cnt_r)
        break
    if x <= 0:
        break

  if rounds:
    print(min(rounds))



#####################

x = int(input())
y = int(input())
p = int(input())

if (y - x) in minimum(x, y - x, p):
    m = minimum(x, y - x, p)[y - x]
else:
    m = False
if ((x == p and not m) or (x < p and not m)) and x < y:
    print(-1)
    exit()


help_F(x,y,p)
