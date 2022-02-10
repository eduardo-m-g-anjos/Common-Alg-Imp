import timeit #only for performance assesment

# Python program to return the Greatest (Highest) Common Divisor (Factor)

def NaiveGDC(x,y):
    a, b = sorted((x,y))
    if b%a==0:
        return a
    for p in reversed(range(a-1)):
        if a%p==0:
            if b%p==0:
                return int(p)
    
def EuclidianGDC_compact(x, y):
    while y:                
        x, y = y, x % y     
    return x

def EuclidianGDC(x,y):
    while y:
        temp = y
        y = x % y
        x = temp
    return x


if __name__=='__main__':
    x, y = 2147482647, 1967562 # >>> 2529
    gdc = []
    
    starttime = timeit.default_timer()
    gdc.append(NaiveGDC(x,y))
    print("Naive GDC:", timeit.default_timer() - starttime)
    
    starttime = timeit.default_timer()
    gdc.append(EuclidianGDC(x,y))
    print("EuclidianGDC:", timeit.default_timer() - starttime)

    starttime = timeit.default_timer()
    gdc.append(EuclidianGDC_compact(x,y))
    print("EuclidianGDC_compact:", timeit.default_timer() - starttime)

    #a "set" is a collection of unique objects, it is like a list but removing repetitions
    assert len(set(gdc))<2, "Different Values! Something is wrong"

    print(gdc[0])