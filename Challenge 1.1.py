# 1.1 Implementation of recursive function to calculate the factorial of a given number
def recursion_factorial(number):  
   if number == 1:  
       return number  
   else:  
       return number*recursion_factorial(number-1)  
# Getting Input from the User  
number = int(input("Enter a number: "))  
# Checking the given number is not lesser than Zero  
if number < 0:  
   print("Negative Integers are non-valid. Give an Positive Integer.")  
#If the given number is equal to Zero
elif number == 0:  
   print("The factorial of 0: 1")  
else:  
   print("The factorial of",number,":",recursion_factorial(number))