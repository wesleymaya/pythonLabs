#Wesley Maya

#Exercise 2
def ask():

    again = "yes"

    while (again == "yes"):

        int1 = int(input("Enter your first integer: "))
        int2 = int(input("Enter your second integer: "))

        sum1 = int1 + int2
    
        print(sum1)
        again = input("Would you like to proform that again?: ")


#Exercise 3
def first_neg(lst):

    j = 0
    
    if lst != []:
        while j in range(0,len(lst)):
            if lst[j] < 0:
                return lst.index(lst[j])
            j += 1

            
    return None

#Exercise 4

#1
def sum_5_consecutive(n):

    
    for i in range(len(n)-4):
        sum1 = n[i] + n[i+1] + n[i+2] + n[i+3] + n[i+4]
        if sum1 == 0:
            return True

    return False

#2
def sum_5_consecutive2(n):

    i = 0
    while i in range(len(n)-4):
        sum1 = n[i] + n[i+1] + n[i+2] + n[i+3] + n[i+4]
        if sum1 == 0:
            return True

        else:
            i += 1

    return False

#Exercise 5
#In creating_various_lists.py file

#Exercise 6
def fib(n):

    a = [1,1]

    for i in range(2,n):
        a.append(a[i-1]+a[i-2])

    return a

#Exercise 7
def innerproduct(n,m):

    j = 0
    
    for i in range(len(m)):
        j += n[i]*m[i]

    return j







        
        
