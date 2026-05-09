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
n = int(input("Enter a no: "))
count = 0
for i in range(1,n+1):
    if n%i==0:
        count=count+1
if count==2:
        print("Prime no")
else:
        print("Not a Prime")