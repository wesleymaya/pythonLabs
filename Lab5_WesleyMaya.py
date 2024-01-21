#Wesley Maya

#Ex 1
def ah(l,x,y):

    lst2 = []
    
    for i in l:
        if i >= x and i <= y:
            lst2 = lst2 + [i]


    sums = len(lst2)
    minn = min(lst2)

    return (sums,minn)


#Ex 2a
def is_perfect(per):

    lstp = []
    
    for i in range(1,per):
        if per%i == 0:
            lstp = lstp + [i]

    if sum(lstp) == per:
        return True

    else:
        return False


#Ex 2b
#Can use for any #(10000, 35000000)
def find_perfects(num):

    for k in range(1,num):
        if is_perfect(k) == True:
            print(k)

        else:
            None


#Ex 3a
def arithmetic(lst1):

    acum = []
    
    for i in range(1, len(lst1)):
        acum = acum + [lst1[i]-lst1[i-1]]

    if acum[0]*len(acum) == sum(acum):
        return True

    else:
        return False


#Ex 3b
def is_sorted(n):

    for j in range(1, len(n)):
        if n[j]-n[j-1] > 0:
            None

        else:
            return False

    return True
                
        

    

    
        
    


