#Lab 7 Exersies

#E1
def indexes(word,let):

    lst = []

    for i in range(len(word)):
        if word[i]==let:
            lst += [i]

    return lst


#E2
def doubles(lst):

    for i in range(len(lst)-1):
        if (lst[i]*2) == lst[i+1]:
            print(lst[i+1])


#E3
def four_letter(wds):

    wds4 = []

    for i in range(len(wds)):
        if len(wds[i]) == 4:
            wds4.append(wds[i])

    return wds4

    
#E4
def inBoth(lst1,lst2):

    for i in lst1:
        if lst2.count(i) >=1:
            return True

    return False

#E5
def intersect(lst1,lst2):

    intes = []

    for i in lst1:
        if lst2.count(i) >=1:
            intes.append(i)
    
    return intes

#Ex6
def pair(lst1,lst2,n):

    for i in lst1:
        for j in lst2:
            if i+j == n:
                print(i,j)


#Ex7
def pairSum(lst1,n):

    t = 0

    for i in range(len(lst1)):
        for j in range(t,len(lst1)):
            if (lst1[i]+lst1[j] == n) and (i != j):
                print(i,j)

        t += 1

#Ex8
def lastfirst(lst1):

    first = []
    last = []
    
    for i in lst1:
        k = i.replace(",","")
        j = k.split()
        first += [j[0]]
        last += [j[1]]

    return [first,last]

#Ex9
def subsetSum(lst1,n):

    
    for i in range(len(lst1)-2):
        for j in range(i+1,len(lst1)-1):
            for k in range(j+1,len(lst1)):
                if lst1[i]+lst1[j]+lst1[k] == n:
                    return True

    return False

#Ex10
def mystery(n):

    i = 0

    while n > 1:
        n = n//2
        i += 1

    return i

#Ex11
def inversions(letts):

    cou = 0

    for i in range(len(letts)):
        for j in range(i+1,len(letts)):
            if ord(letts[i]) > ord(letts[j]):
                cou += 1

    return cou

#Ex12
def sublist(lst1,lst2):

##    newl = []
##
##    for i in range(len(lst1)):
##        if 
