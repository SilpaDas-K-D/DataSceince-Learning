''' Write a program to print the reverse of a number'''

num = str(input("Enter a number : "))

# 1. Using slicing method 

print("reverse of the number is : ",num[::-1])

#2 . Using while loop 

num = 1234
rev_num = ''

while(num > 0):
    rem = num %10
    rev_num += str(rem)
    num = num //10
print("reverse no isss ", rev_num)
