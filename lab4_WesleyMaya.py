#Wesley Maya

#Question 1
def is_eligible(age,citizenship,prison):

     '''
     (int,string,string) -> (boolean)

     Description
     This function returns whether you are eligible to vote in Canada.

     Pre-Conditions
     None.
     '''
     
     if age >=18:
         if citizenship == "canada":
             if prison == "no":
                return True
     else:
          return False
     
name=input("What is your name? ")
name = name.lower()
age= int(input("How old are you? "))
citizenship = input("What country are you from?: ")
citizenship = citizenship.lower()
prison = input("Have you been to prison?: ")
prison = prison.lower()

if is_eligible(age,citizenship,prison) == True:
     print(name, ", you are eligible to vote")
else:
     print(name, ", you are ineligible to vote")


#Question 2
def mess(string1):
     
    '''
    (str) -> str

    Description
    This function takes a String and returns that string, but capitalizes any letters in the string that are in the string "rstvwxyz".

    Pre-Conditions
    string1 must be a String.
    '''
    
    string2 = ""

    for character in string1:
        if character == " ":
            string2 = string2 + '-'
        #if 's' in "silly"
        elif character in "rstvwxyz":
            string2 = string2 + character.upper()
        else:
            string2 = string2 + character


    return string2


#Question 3
def is_divisible(n,m):
     
     '''
     (int, int)->bool

     Description
     Returns True if n is divisible by n, and False otherwise.
     '''
     
     return n%m==0

def is_divisible23n8(n):

     '''
     (int)->bool

     Description
     Returns string "yes" if n is divisible by 2 or 3 but not 8, and "no" otherwise.
     '''
     
     if ( (is_divisible(n,2) or is_divisible(n,3)) and not(is_divisible(n,8))):
          return True
     else:
          return False

def print_all_23n8(num):

    '''
    (str) -> None

    Description
    This function prints out whether the numbers from 0 to num are divisble by 2,3, or 8. 
    
    '''
    
    for i in range(num):
        print(i, is_divisible23n8(i))

user_number = int(input("A non-negative number: "))
print_all_23n8(user_number)



user_input = input("Welcome to python")

result = mess(user_input)

print(result)


#Question 4
def pyrimid(num):

    '''
    (int) -> None

    Description
    This function prints out a pyramid of height num.

    Pre-Conditions
    num must be an int
    
    '''

    for i in range(1,num,2):
        print(i*"#")


#Question 5
def prime(num):

    '''
    (int) -> (boolean)

    Description
    This function returns whether num is a prime number or not in the form of a boolean.

    Pre-Condition
    num must be > 0.
    '''

    
    for i in range(2, n):
        if n%i==0:
            return "Not prime"
        else:
            return "Is prime"


n = int(input("Input a positive number: "))

s = prime(n)

print(s)

