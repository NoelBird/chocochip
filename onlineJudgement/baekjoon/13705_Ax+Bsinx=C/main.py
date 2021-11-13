import math

A, B, C = map(int, input().split())

limit_delta = 10**-7
f = lambda x:A*x + B*math.sin(x) - C
l_bound = C/A-1/A
m_bound = C/A
u_bound = C/A+1/A
while True:
    if f(l_bound)*f(m_bound) < 0:
        u_bound = m_bound
        m_bound = (u_bound + l_bound)/2
    elif f(m_bound)*f(u_bound) < 0:
        l_bound = m_bound
        m_bound = (u_bound + l_bound)/2
    else:
        if l_bound == 0:
            x = l_bound
            break
        elif m_bound == 0:
            x = m_bound
            break
        else:
            x = u_bound
            break
    if abs(f(m_bound)-f(l_bound)) < abs(f(m_bound + limit_delta) - f(m_bound)):
        x = m_bound
        print(f(m_bound))
        break

print(round(x, 6))
