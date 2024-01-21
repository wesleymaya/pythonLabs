#Wesley Maya

#Question 1
def repeater(s1,s2,n):

    concat = s1 + s2

    reap = concat*n

    return '_'+reap+'_'


#Question 2
def roots(a,b,c):

    import math

    delta = b**2-4*a*c
    
    posroot = (-b+(math.sqrt(b**2-4*a*c)))/2*a

    negroot = (-b-(math.sqrt(b**2-4*a*c)))/2*a


    print('This quadratic equation with the coefficents a = '+str(a)+' b = '+str(b)+' c = '+str(c)+' has the roots: '+str(posroot)+' and '+str(negroot)+'.')


#Question 3
def real_roots(a,b,c):

    delta = b**2-4*a*c

    return delta>0


#Question 4
def reverse(x):

    a = x//10
    b = x%10*10

    return a+b
    
