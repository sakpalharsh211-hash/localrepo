# Armstrong Number
def armstrong():
    num=int(input('enter number to check for armstrong '))
    d=len(str(num))
    f=num
    s=0          #zero h o nhi
    while(f>0):
        digit=f%10
        s+=(digit**d) #s=s+(digit**d)
        f=f//10

    if(s==num):
        print('%d is an armstrong number '%num)
    else:
        print('%d is not a armstrong number '%num)
armstrong()

# palindrome
def ispalindrome():
    num=int(input("Enter a number:"))
    temp=num
    rev=0
    while(num>0):
        dig=num%10
        rev=rev*10+dig
        num=num//10
    if(temp==rev):
        print("The number is palindrome!")
    else:
        print("Not a palindrome!")

ispalindrome()


        
