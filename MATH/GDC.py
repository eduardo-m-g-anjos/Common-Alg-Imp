import timeit #only for performance assesment
import prime_sieve
# Python program to return the Greatest (Highest) Common Divisor (Factor)

def NaiveGDC(x,y):
    a, b = sorted((x,y))
    if b%a==0:
        return a
    primes = prime_sieve.SieveOfEratosthenes(a)
    for p in primes:
        if a%p==0:
            if b%p==0:
                return int(a/p)
    

if __name__=='__main__':
    x, y = 2147482647, 1967562

    starttime = timeit.default_timer()
    naive_GDC = NaiveGDC(x,y)
    print("Naive GDC:", timeit.default_timer() - starttime)
    

    #assert
    print(naive_GDC)