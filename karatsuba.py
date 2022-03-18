import timeit

runk = '''

def karatsuba(x, y):
    x = 2.0
    y = 3.0
    if len(str(x)) or len(str(y)) == 1:
        return x * y 
    else: 
        n = max(len(str(x)), len(str(y)))
        nby2 = n / 2
        a = x / 10**(nby2)
        b = x % 10**(nby2)
        c = y / 10**(nby2)
        d = y % 10**(nby2)
        
        ac = karatsuba(a, c)
        bd = karatsuba(b, d)
        ad_plus_bc = karatsuba(a+b, c+d) - ac - bd

       	# this little trick, writing n as 2*nby2 takes care of both even and odd n
        # prod = ac * 10**(2*nby2) + (ad_plus_bc * 10**nby2) + bd
        # return prod
    '''

print("""
      \nFirst, Karatsuba's run: 
      """)
print(timeit.timeit(setup = runk, stmt = runk, number = 100000))
 
mult = '''
def normal_mult(n, m):
    n = 4
    m = 4
    if m == 0:
        return 0
    elif m < 0:
        return n - n(m+1)
    else:
        return n + n(m-1)
    '''


print("""
      \nNow, hard-code's run: 
      """)
print(timeit.timeit(setup= mult, stmt = mult, number = 100000))


