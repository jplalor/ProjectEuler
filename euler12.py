#euler problem 12

def triNum(n):
    num = 0
    for i in range(n+1):
        num += i
    return num
    #if n == 1:
        #return 1
    #else:
        #return n + triNum(n-1)

def euler12(n):
    counter = 1
    newNum = triNum(n)
    for i in range(1,newNum/2 + 1):
        if newNum % i == 0:
            counter += 1
    if counter < 500:
        euler12(n+1)
    else:
        print(newNum)

def euler12try2(n):
    import math
    
    for j in range(1, int(math.sqrt(triNum)+1)):
        if triNum % j == 0:
            divisors += 2
    if divisors < 500:
        return euler12try2(n+1)
    else:
        return triNum
        
