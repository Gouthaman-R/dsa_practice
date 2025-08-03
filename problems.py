# def pal(s):
#     if s==s[::-1]:
#         return True
#     else:
#         return False
# print(pal("madam"))

# def fibonacci(n):
#     a=0
#     b=1
#     for i in range(n):
#         print(a,end=" ")
#         a,b=b,a+b
# fibonacci(9)


# def prime(num):
#     if num<1:
#         return False
#     for i in range(2,int(num**0.5)+1):
#         if num%i==0:
#             return False
        
#     return True
        
# print(prime(9))


# def prime(num1,num2):
#     for num in range(num1,num2+1):
#         if num>1:
#             for i in range(2,int(num**0.5)+1):
#                 if num%i==0:
#                     break
#             else:
#                 print(num,end=" ")
# prime(1,10)



# def prime(num1,num2):
#     for i in range(num1,num2+1):
#         if i>1:
#             for j in range(2,int(i**0.5)+1):
#                 if i%j==0:
#                     break
#             else:
#                 print(i,end=" ")
# prime(10,30)



# write a program which takes two values x and y. print x for y number of times

""" input:
    2
    3

    output:
    2
    2
    2
"""
# solution:


# a=int(input("Enter the no.1:"))
# b=int(input("Enter the no.2:"))
# for i in range(b):
#     print(a)


"""Write a program to get firstName and lastName and n as input and print fullName that is firstName+lastName for n times.

Input

Nandy

Raja

5

Expected output:

NandyRaja

NandyRaja

NandyRaja

NandyRaja

NandyRaja"""

# solution

# a=str(input("first_name:"))
# b=str(input("last_name:"))
# c=int(input("enter the number:"))
# d=a+b
# for i in range(c):
#     print(d)



"""Write a program to take x and print multiples of x till 1000.

Input:

100

Expected Output:

100

200

300

400

500

600

700

800

900

1000 """

# solution

x = int(input("Enter value of x: "))
n = 1

while x * n <= 1000:
    print(x * n)
    n += 1
