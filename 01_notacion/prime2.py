 

# taking input from user
number = int(input("Enter any number: "))

# prime number is always greater than 1
boolprime=True
if number > 1:
    for i in range(2, number*0.5):
        if (number % i) == 0:
	    boolprime= False
 
    if boolprime:
        print(number, "is a prime number")
    else:
        print(number, "is not a prime number")   
# if the entered number is less than or equal to 1
# then it is not prime number
else:
    
    print(number, "is not a prime number")
