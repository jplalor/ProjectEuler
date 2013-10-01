import math

def euler9():
	#finalAnswer = False
    #while finalAnswer == False:
    triples = []
    for a in range(1,500):
        for b in range(1,500):
            c = math.sqrt(a**2 + b**2)
            if a+b+c == 1000:
                return a,b,c,a*b*c
    #while a < 1000:
        #while b < 1000:
            #c = math.sqrt(a*a + b*b)
            #if c % 1 ==0:
                #print c
            #if a+b+c == 1000:
                #return a*b*c
            #b += 1
        #a +=1
    nogood = "it didnt work"
    return nogood

	#psum = 1000
	#a = 0
	#b = 0
	#c = math.sqrt(a*a + b*b)
	#psum = a+b+c
	#return a, b, c, psum2
