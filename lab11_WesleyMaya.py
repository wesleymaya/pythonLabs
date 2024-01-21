#Ex 1
def m(i):

    if i > 0:
        t = (i/((2*i)+1))
        return m(i-1)+t

    else:
        return 0

#Ex 2
def count_digits(num):

    if num//10 > 0:
        return count_digits(num//10)+1

    else:
        return 1

#Ex 3
def is_palindrome(word):

    if len(word) > 0 and word[0].lower() == word[len(word)-1].lower():
        ans = is_palindrome(word[0+1:len(word)-1])
        return ans


    elif len(word) > 1:
        return False

    else:
        return True


#Ex 4
def is_palindrome_v2(word):

    if len(word)>0 and (word[0].isalpha() == True and word[len(word)-1].isalpha() == True) and (word[0].lower() == word[len(word)-1].lower()):
        ans = is_palindrome_v2(word[0+1:len(word)-1])
        return ans

    elif len(word)>0 and (word[0].lower() != word[len(word)-1].lower()):
    
        if word[0].isalpha() != True:
            ans2 = is_palindrome_v2(word[0+1:len(word)])
            return ans2

        if word[len(word)-1].isalpha() != True:
            ans3 = is_palindrome_v2(word[0:len(word)-1])
            return ans3

        else:
            return False


    elif len(word) > 1:
        return False

    else:
        return True


#Ex 5
def gcd(a,b):

    c = a%b
    
    if c > 0:
        ans = gcd(b,c)
        return ans

    else:
        return b
        
