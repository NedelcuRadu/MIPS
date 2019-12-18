def ciframax(n):
    max = 0
    while n > 0:
        c = n % 10
        if c > max:
            max = c
        n = n // 10
    return max

def alipire(*args):
    y=0
    for x in args:
       y=y*10+ciframax(x)
    return y

def pctb(a,b,c):
    if alipire(a)>2 or alipire(b)>2 or alipire(c)>2:
        return False
    return True
