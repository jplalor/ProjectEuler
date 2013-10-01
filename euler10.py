def euler10():
    isPrime = True
    sum = 0
    for x in range (2, 2000000):
        for y in range(2, x):
            if x % y == 0:
                isPrime = False
                break
        if isPrime:
            sum+= x
    return sum
