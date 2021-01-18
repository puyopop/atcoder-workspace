# https://en.wikipedia.org/wiki/Cycle_detection
def floyd_cycle_finding(f, x0):
    '''
    循環していない部分の長さをlam
    循環部分の長さをmuとして
    (lam, mu)
    を返す
    >>> floyd_cycle_finding(lambda x: x**2 % 3, 2)
    (1, 1)
    >>> floyd_cycle_finding(lambda x: x**2 % 1001, 2)
    (2, 4)
    >>> floyd_cycle_finding(lambda x: x**2 % 16, 2)
    (2, 1)
    >>> floyd_cycle_finding(lambda x: x*2 % 5, 3)
    (0, 4)
    >>> floyd_cycle_finding(lambda x: x*2 % 5, 0)
    (0, 1)
    '''
    # a_i = a_j
    # の関係が成り立つ時
    # a_{lam+n+k*mu} = a_{lam+n+k'*mu}
    # より|i-j|は循環の長さの整数倍になる
    # そこで
    # a_m = a_2m
    # なるmを見つける
    # 前述の性質からmは循環の長さの整数倍となっているため
    # 2m - m = m = k*mu = lam + n + k'*mu
    # したがって、lam + nはmuの倍数となるので
    # 地点mからlamステップ進むと循環の開始点に到達する
    # lamが求まれば後は流れでmuも求まる
    
    tortoise = f(x0)
    hare = f(f(x0))
    while tortoise != hare:
        tortoise = f(tortoise)
        hare = f(f(hare))
    lam = 0
    tortoise = x0
    while tortoise != hare:
        tortoise = f(tortoise)
        hare = f(hare)
        lam += 1
    mu = 1
    hare = f(tortoise)
    while tortoise != hare:
        hare = f(hare)
        mu += 1
    return lam, mu
