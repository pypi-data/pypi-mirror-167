# Check if the number is Odd or Even

def isoddeven(n):
    if n==0:
        print("Zero")
    elif(n%2==0):
        print("Even")
    else:
        print("Odd")
 
 
 # Check if the number is Palindrome or not.
        
def isPalindrome(i):
    
        temp,rev=i,0
        while(i > 0):  
            dig = i % 10  
            rev = rev * 10 + dig
            i = i//10
        if temp==rev:
            print("Palindrome")
        else:
            print("Not Palindrome")


#Check if the number is Armstrong or not.


def isArmstrong(num):
    
        order = len(str(num))

        sum = 0

        temp = num
        while(temp>0):
            digit = temp % 10
            sum += digit ** order
            temp //= 10

        if num == sum:
            print("Armstrong")
        else:
            print("Not Armstrong")


# Check if the number is Prime number or not

def isPrime(num):
    if num > 1: 
        for i in range(2,num):
            if (num % i) == 0:
                print("Not Prime")
                break
        else:
            print("Prime ")
       
    else:
        print("Not Prime")
        