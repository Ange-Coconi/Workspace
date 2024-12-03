a = 2
def test(x,y):
    poids = (x + y) * a
    return(poids)

for i in range(12,-1,-2):
    print(i)
        
import math
sign = math.copysign(3, a)

def signe(a):
    if a > 0:
        return(str(a)+' est positif')
    elif a == 0:
        return(str(a)+' est nul')
    else:
        return(str(a)+' est négatif')
    
def fibonacci(n):
    a=0
    f=0
    f2=1
    print(f)
    print(f2)
    while a < n:
        f3 = f
        f = f + f2
        f2 = f3
        a+=1
        print(f)
        
