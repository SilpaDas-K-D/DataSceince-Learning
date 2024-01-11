''' write a program to check whether a no is even or odd '''

num = int(input("enter a number :"))

# First method

if num%2 ==0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")

# second method
    
print("even") if num%2==0 else print("odd")
