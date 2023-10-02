# To determines whether the given year is a leap year or not using ifelif-else statements.
def CheckLeap(Year):  
  # Checking if the given year is leap year  
  if((Year % 400 == 0) or  
     (Year % 100 != 0) and  
     (Year % 4 == 0)):   
    print(Year,"Year is a leap Year")  
  # Else it is not a leap year  
  else:  
    print ( Year,"Year is not a leap Year")  
# Taking an input year from user  
Year = int(input("Enter the Year : "))  
# Printing result  
CheckLeap(Year)