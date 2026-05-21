'''

stu_marks = int(input("Enter marks:"))
if stu_marks >= 90:
    print("A+")
elif stu_marks >= 80:
      print("A")
elif stu_marks >= 70:
    print("B+")
elif stu_marks >= 60:
    print("B")
elif stu_marks >= 50:
    print("C+")
elif stu_marks >= 35:
    print("Pass")
else:
    print("Failed")


a = 8
b = 5
c = 90
if a > b and c:
    print(a)
elif b > a and c:
    print(b)
else:
    print(c)
    
    

SBI_bank ={"ATM PIN": "66000"}
pin = input("Enter 4 digit ATM pin: ")
if len(str(pin)) == 4:
    if pin in SBI_bank['ATM PIN']:
        print("Welcome to SBI ATM")

    else:
        print("Invalid pin")
        
else:
    print("pls enter 4 digit pin")


for statement
-------------
-->used to itterate over a sequence



any = "Python"
an = [1,2,3,4]
so = (5,6,7,8)
for how in any:
    print(how)


range()
-------
range() is in-built function used to generate number in sequence manner

syntax---> range(start,end,step)

else in for
-----------
-->once the itterations completed this else will be

break
-----
-->used to exit from the loop based on the condition

continue
--------
-->used to skip the current itteration based on the condition


for i in range(1,10):
    print(i)
    if i == 5:
        break

for i in range(1,10):
    if i == 5:
        continue
    print(i)


for i in range(1,10):
    if i == 3:
        pass
while is ---> for + if

i = 1
while i < 5:
    print(i)
    i += 1

    











    

