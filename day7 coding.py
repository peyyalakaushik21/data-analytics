'''
f-string
--------

Conditional statements
----------------------
if--> to check whether statement is true or not

if-else--> else in the if statement,

incase the condition becomes false then it will enter into
fall-back(else), it will execute whatever inside it

nested if
elif


num = int(input())
if num%2 == 0:
    print(f"{num} is an even number")

else:
     print(f"{num} is an odd number")

     age = int(input("Enter the age: "))
     if age >= 18:
       print("you are eligible to vote")
      
else:
    print(f"you have to wait for {18-age} more years")

num = int(input("Enter the number1: "))
num_2 = int(input("Enter the number2:"))
if num > num_2:
    print(f"{num} is greater number than {num_2})
          
eg:

else:
     print(f"{num_2} is greater than {num}")
     year = int(input("Enter the year to know if it is leap year or not: "))

eg:

if (year%4 == 0 and year%100 != 0)or (year %400 == 0):
    print(f"{year} is a leap year")
          
eg:
         
else:
     print(f"{year} is not a leap year")


vowel = input("Enter the character to check if it is vowel: ")
if vowel in "aeiouAEIOU":
    print(f"{vowel} is a vowel")

else:
     print(f"{vowel} is a consonent")

     num = int(input("Enter number: "))
     if num >= 0:
     print(f"{num} is a positive number")
else:
     print(f"{num} is a negative number")



marks = int(input("Enter your marks: "))
stu_name = input(Enter your name: ")

if marks >=45:
    print(f"{stu_name} you passed.")
    
else:
    print(f"{stu_name} you failed.")


num = int(input("Enter number: "))

if num%3 == 0 and num%5 == 0:
    print(f"{num} is divisible by 3 and 5")

else:
     print(f"{num} not")



signal = int(input("Enter \n1.Red \n2.green \n: "))

if signal == 1:
    print("Stop!!!")

else:
    print("GO")
 
  

i         



















                           
