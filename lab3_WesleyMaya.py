#Wesley Maya

#Question 1
def pay(wagehr, hrs):
    
    '''
    (float,float) -> (float)
    
    Description:
    This function will recieve 2 floats and return the wage (as a float) earned by the user.

    Pre-Conditions:
    wagehr and hrs must be real numbers.
    '''
    
    if hrs <= 40:
        wage = wagehr*hrs
    else:
        if hrs > 40 and hrs <= 60:
            wage =(wagehr*40)+(wagehr*(hrs-40)*1.5)
        else:
            if hrs > 60:
                wage =(wagehr*40)+(wagehr*(20)*1.5)+(wagehr*(hrs-60)*2)

    return wage


#Question 2
def rps(first, second):

    '''
    (str,str) -> (int)
    
    Description:
    This function will recieve two strings, one of player one and another of player two; representing rock, paper, or sissors and return the score of if player 1 beat player 2.

    Pre-Conditions:
    first == "R" or "P" or "S"
    second == "R" or "P" or "S"
    '''

    if (first == second):
        return 0
    else:
        if (first == "R" and second == "S") or (first == "P" and second == "R") or (first == "S" and second == "P"):
            return 1
        else:
            return -1


#Question 3a
def is_divisible(n,m):

    '''
    (int,int) -> (bool)
    
    Description:
    This function will recieve 2 int and return whether the divison of n and m creates a remainder, true for no, and false for yes.

    Pre-Conditions:
    None
    '''

    
    divs = (n%m == 0)
    if divs:
        return divs

n = int(input("What is the first integer?: "))
m = int(input("What is the second integer?: "))

result = is_divisible(n,m)

if result == True:
    print(str(n),"is divisable by",str(m))
else:
   print(str(n),"is not divisable by",str(m))



#Question 3b
def is_divisible_23n8(n):

    '''
    (int) -> (str)
    
    Description:
    This function will recieve an integer and see if it is divisible by 2 or 3, but as well, not by 8. Then, will return yes or no depending on answer.

    Pre-Conditions:
    None
    '''

    if (is_divisible(n,2) or is_divisible(n,3)) and not is_divisible(n,8):
        return "Yes"
    else:
        return "No"



n = int(input("Enter an integer: "))

result = is_divisible_23n8(n)

if (is_divisible_23n8(n) == "Yes"):
    print(n,"is divisible by 2 or 3, but not 8")
else:
    print(n,"is not divisible by 2 or 3, but not 8")
    
        
    





    
        



