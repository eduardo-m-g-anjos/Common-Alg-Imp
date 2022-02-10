import timeit #only for performance assesment

# Python program to return all primes smaller than or equal to n

def NaivePrimes(n):
    res = []
    if n>=2:
        for i in range(2, n):
            p = True
            for j in range(2,int(i/2)+1):
                if i%j==0:
                    p = False
                    break
            if p:
                res.append(i)
    return res

def SieveOfEratosthenes(n):    
    # Everithing is a prime unless proven other way
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):
            for i in range(p ** 2, n + 1, p): #if is a multiple of p, is divisible by p, so not a prime
                prime[i] = False 
        p += 1
    prime[0]= False
    prime[1]= False # https://www.wgtn.ac.nz/science/ask-a-researcher/is-1-a-prime-number

    res = []
    for p in range(n + 1):
        if prime[p]:
            res.append(p)
    return res
 
if __name__=='__main__':
    n = 100000

    starttime = timeit.default_timer()
    naive_primes = NaivePrimes(n)
    print("Naive Prime:", timeit.default_timer() - starttime)

    starttime = timeit.default_timer()
    erastosthenes_primes = SieveOfEratosthenes(n)
    print("Sieve of Erastosthes:", timeit.default_timer() - starttime)
    
    assert erastosthenes_primes==naive_primes, "Different Values! Something is wrong"
    #print("Following are the prime numbers smaller than or equal to {} \n {}".format(n,erastosthenes_primes))
