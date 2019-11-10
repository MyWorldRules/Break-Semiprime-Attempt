import sympy

def solve(val):
    iterations = 0
    thePrime = sympy.prevprime(val)
    
    while not sympy.isprime((int) (val/thePrime)):
        thePrime = sympy.prevprime(thePrime)
        iterations+=1
        if iterations%10000 == 0:
            print(iterations)
    return thePrime, (int) (val/thePrime), iterations

print(solve(340282366920938464385711811117245792737))

#print(solve(9))

#Testing
#print (sympy.isprime(5))
#print(sympy.prevprime(340282366920938464385711811117245792737))
