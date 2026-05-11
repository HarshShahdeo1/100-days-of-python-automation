# n = int(input("Enter a number: "))
# fact = 1
# for i in range(1,n+1):
#     fact=fact*i
# print(f"Te factorisl {n} natural number is: {fact}")
# n=int(input("Enter a number: "))
# a=0
# b=1
# for i in range(0,n):
#     c=a+b
#     a=b
#     b=c
# print("The febonacci no are: ",a)
# n = int(input("Enter a number: "))

# for i in range(1,n+1):
#     if n%i == 0:
#         print(i)
# n = int(input("Enter a no: "))
# count = 0
# for i in range(1,n+1):
#     if n%i==0:
#         count=count+1
# if count==2:
#         print("Prime no")
# else:
#         print("Not a Prime")
# row = int(input("Enter the value of row: "))
# col = int(input("Enter the value of col: "))
# for i in range(1,row):
#     for j in range(1,col):
#         print(i,",",j, end="  ")
#     print(" ")
# for n in range(1,101):
#         count = 0
#         for i in range(1,n+1):
#             if n%i==0:
#                 count = count+1
#         if count == 2:
#              print(n)
# for i in range(1,6):
#     for j in range(1,6):
#         print("*",end=" ")
#     print(" ")
# Method 1
# for i in range(1,7):
#     for j in range(1,7):
#         if i>=j:
#             print("*",end=" ")
#     print(" ")
#Method 2
# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print(" ")
#Method 3
# for i in range(5,0,-1):
#     print("*" *i)
# for i in range(1,6):
#     for j in range(1,6):
#         if j>=i:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print(" ")
s1="Hello World"
print(s1[3:7])
