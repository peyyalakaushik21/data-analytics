'''

for i in range(1,10):
    for j in range(1,2):
         print(i)
         print(j)


nmu = 9
for j in range(1,11):
    print(f"{num} x {j} = {j*num}")


so = input("Enter a word")
empty_str = ""
for j in so:
    empty_str = j + empty_str
    print(empty_str)
if empty_str == so:
    print(f"{so} is palindrome")
else:
    print(f"{so} is not a palindrome")
    
    

num = int(input("Enter a number: "))
amstro_ = 0
length_ = len(str(num))
for i in str(num):
    amstro_ += int(i) ** length_
if amstrong_ == num:
    print(f"{num} is an amstrong number)")
else:
    print(f"{num} is not an amstrong number")




num = int(input("Enter a perfect number: "))
per_num  = 0
for j in range(1,num):
    if num % j == 0:
        per_num +=j
if per_num == num:
    print(f"{num} is a perfect num")
else:
    print(f"{num} is not a perfect num")



num = int(input("Enter a number: "))
for k in range(1, num):
    if num % k == 0:
        count += 1
if count == 2:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")
    
        
    

star_ = 5
for g in range(1,star_+1):
    for d in range(1,g+1):
        print("*", end="")
        print()



star_ = 5
count = 0
for g in range(star_,0,-1):
    for d in range(1,g+1):
        count += 1
        print(chr(64+d), end=" ")
    print()



'''
num = 5
for j in range(1,num+1):
    print(" "*(num-j),end="")
    for i in range(1,j+1):
        print("*",end=" ")
    print()








































