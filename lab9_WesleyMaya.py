#Lab 9

#Exersise 1a
def letter2number(lgrade):

    system = {"A+":10,"A":9,"A-":8,"B+":7,"B":6,"C+":5,"C":4,"D+":3,"D":2,"E":1,"F":0}
    
    return system[lgrade]


#Exersise 1b
def letter2number2(lgrade):

    if lgrade == "A+":
        return 10
    elif lgrade == "A":
        return 9
    elif lgrade == "A-":
        return 8
    elif lgrade == "B+":
        return 7
    elif lgrade == "B":
        return 6
    elif lgrade == "C+":
        return 5
    elif lgrade == "C":
        return 4
    elif lgrade == "D+":
        return 3
    elif lgrade == "D":
        return 2
    elif lgrade == "E":
        return 1
    elif lgrade == "F":
        return 0
    
#Exersise 2
def agencies():

    age = {"CCC":"Civilian Conservation Corps","FCC":"Federal Communications Comission","FDIC":"Federal Deposit Insurance Corporation","SSB":"Social Security Board","WPA":"Works Progress Adminsitration"}

    age["SEC"] = "Securities and Exchange Commission"
    age["SSB"] = "Social Securites Administration"
    del age["CCC"]
    del age["WPA"]

    print("This dict has been edited")


#Exercise 6.5a
def lookupEx():

    phonebook = {("Johnny","Test"):['519-422-6331'],("Gordon","Ramsey"):['334-266-3541'],("Mike","Trout"):'416-665-9924'}

    first = input("Enter the first name: ")
    last = input("Enter the last name: ")

    ans = phonebook.get((first,last),"Sorry, this person doesn't exist in our book")

    return ans


#Exercise 3
def lookup(phonebook):
    
    while True:
        first = input("Enter the first name: ")
        last = input("Enter the last name: ")
        
        ans = phonebook.get((first,last),"None")

        if ans == "None":
            print("Sorry, this person doesn't exist in our book")

        else:
            break

    for i in phonebook[(first,last)]:
        print(i)

#phonebook1 = {("Johnny","Test"):['519-422-6331','416-665-9924'],("Gordon","Ramsey"):['334-266-3541','442-995-9926'],("Mike","Trout"):['443-112-3456','123-456-7890']}
#lookup(phonebook1)
            
#Exercise 4
def reverse(phbook):

    phbook2 = {}

    for k in phbook:
        v = phbook[k]
        phbook2[k] = v

    return phbook2

#Exercise 0
def get_year():

    try:
        j = int(input("Input an integer: "))
        if len(str(j)) == 4:
            return (j)

        else:
            print("This isn't a 4 digit integer, please try again")
            return get_year()
    
    except ValueError:
        print("This isn't a 4 digit integer, please try again")
        return get_year()

#get_year()


#Slides
#Exercise 2
def min_or_max(lst,bool1):

    if bool1 == True:
        min1 = lst[0]
        for i in lst:
            if i < min1:
                min1 = i

        return min1

    else:
        if bool1 == False:
            max1 = lst[0]
            for j in lst:
                if j > max1:
                    max1 = j

            return max1

#Ex 3a
def first_one(lst):

    a = 0
    b = len(lst)-1

    if lst[0] == 1:
        return 0

    while (b-a)+1 >3:
        mid = (b+a)//2
        if lst[mid] == 0 and lst[mid+1]==1:
            return mid+1
        
        elif lst[mid] == 0:
            a = a + mid
            
        else:
            if lst[mid] == 1:
                b = b - mid


    while (b-a) >= 0:
        mid = (b+a)//2
        if lst[mid] == 1:
            return a

        else:
            a = a + 1

    return -1


#Ex 3b
def last_zero(lst):

    res = first_one(lst)

    if res == 0:
        return -1

    elif res == -1:
        return len(lst)+res

    else:
        return res -1
    
    

    
    
