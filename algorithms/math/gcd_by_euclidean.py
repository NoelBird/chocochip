# it came from fractions.gcd code
# but recently, math.gcd is used to calculate gcd
# so if you want to code with python, then use below code
# else use math.gcd()

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a