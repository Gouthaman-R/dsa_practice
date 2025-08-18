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

# =======================================================================================================

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


# =======================================================================================================

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


# =======================================================================================================


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

# x = int(input("Enter value of x: "))
# n = 1

# while x * n <= 1000:
#     print(x * n)
#     n += 1


# =======================================================================================================
"""
Prob 1 : Write a program that takes an integer, then a string, then a char from the user and prints them in the screen.


Input:  2 Name y

Expected Output:

2

Name

y

"""
#  solution 
# a= (input("enter the number"))
# b=(input("enter the name:"))
# c=(input("enter the letter:"))
# print(a,'\n'+b,'\n'+c)


# =======================================================================================================

"""
Prob 2: Write a program to check whether a triangle can be formed with the given values for the angles.

If sum of angles is equal to 180, then triangle can be formed, else it can't be formed.

Input: 45 45 45

Expected Output: 

Triangle cannot be formed

Explanation -> We are getting 3 inputs, that is three angles of triangle, but here the sum of three angles that is 45+45+45 is not equal to 180 so Triangle cannot be formed is the output.

"""
# solution

# def triangle(a,b,c):
#     sum=a+b+c
#     if sum==180:
#         print("can form triangle")
#     else:
#         print("cannot form triangle")
# a=int(input("enter the number:"))
# b=int(input("enter the number:"))
# c=int(input("enter the number:"))
# triangle(a,b,c)


# =======================================================================================================

"""Given mark of student, Print the Grade

Grade A if mark is greater than or equal to 90

Grade B if mark is greater than or equal to 80

Grade C if mark if greater than or equal to 60

Grade D if mark if greaer than or equal to 35

Fail if mark is lesser than 35


Input: 95

Expected Output:

Grade A
"""

# solution

# mark=int(input("enter the mark:"))
# if mark>=90 and mark<=100:
#     print("grade A")
# elif mark>=80 and mark<90:
#     print("grade B")
# elif mark>=60 and mark<80:
#     print("grade C")
# elif mark>=35 and mark<60:
#     print("grade D")
# elif mark<35 and mark>=0:
#     print("fail")
# else:
#     print("invalid mark")

# =============================================================================================================


# n=5
# for i in range(0,n):
#     for j in range(0,n):
#         print("*",end=" ")
#     print("")

# output

"""
* * * * * 
* * * * *
* * * * *
* * * * *
* * * * *

"""

# =============================================================================================================

# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(j,end=" ")
#     print("")
# solution

"""
1 2 3 4 5 
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5

"""
# =============================================================================================================

# n=5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print(" ")

# output

"""
1  
1 2
1 2 3
1 2 3 4
1 2 3 4 5

"""
# =============================================================================================================
# n=3
# for i in range(1):
#     for j in range(1,n+1):
#         print(j*"*",end=" ")


# n=5
# for i in range(1,n+1):
#     print(i*"*",end=" ")

# output
"""
* ** *** **** ***** 
"""
    
# =============================================================================================================


# n=6
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(j,end=" ")
#     print("")
#     n-=1

# output
"""
1 2 3 4 5 6 
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
"""

# =============================================================================================================

# n=6
# for i in range(1,n+1):
#     for j in range(1,n-i+2):
#         print("*",end="")
#     print("")

# output
"""
******
*****
****
***
**
*
"""

# =============================================================================================================
# n=6
# for i in range(1,n+1):
#     for j in range(n,0,-1):
#         print(j,end="")
#     print("")
#     n-=1

# output
"""
654321
54321
4321
321
21
1

"""

# =============================================================================================================

# n=6
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end="")
#     print("")

# output
"""
*
**
***
****
*****
******
"""
# =============================================================================================================

# example-1
# n=6
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end="")
#     print("")

# for i in range(1,n+1):
#     for j in range(1,n-i+1):
#         print("*",end="")
#     print("")

# example-2(more optimized)

# n=10
# for i in range(1,n+1): 
#     print(i*"* ")
        
# for j in range(n-1,0,-1):
#     print(j*"* ")

# output
"""
* 
* *
* * *
* * * *
* * * * *
* * * * * *
* * * * *
* * * *
* * *
* *
*

"""

# =============================================================================================================
# n=4
# for i in range(1,n+1):
#     for j in range(1,n+1-i):
#         print(" ",end=" ")
#     for K in range(1,2*i+1-1):
#         print("*",end=" ")
#     print("")
    
# solution
"""
      * 
    * * *
  * * * * *
* * * * * * *

"""

# =============================================================================================================

# n=4
# for i in range(1,n+1):
#     for j in range(1,i):
#         print(" ",end=" ")
#     for j in range(1,(2*n+1)-(2*i-1)):
#         print("*",end=" ")
#     print("")

# output

"""
* * * * * * * 
  * * * * *
    * * *
      *

"""
# =============================================================================================================


# n=6
# for i in range(1,n+1):
#     for j in range(1,n+1-i):
#         print(" ",end=" ")
#     for K in range(1,2*i+1-1):
#         print("*",end=" ")
#     print("")
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(" ",end=" ")
#     for j in range(1,2*n+1-2*i-1):
#         print("*",end=" ")
#     print("")

# output
"""
          * 
        * * *
      * * * * *
    * * * * * * *
  * * * * * * * * *
* * * * * * * * * * *
  * * * * * * * * *
    * * * * * * *
      * * * * *
        * * *
          *


"""

# =============================================================================================================

# n=6
# count=1
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(count,end=" ",)
#         count+=1
#     print("")

# output

"""
1 
2 3
4 5 6
7 8 9 10
11 12 13 14 15
16 17 18 19 20 21

"""

# =============================================================================================================


# n=6
# count=1
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(count,end=" ")
#     count+=1
#     print("")

# output
"""
1 
2 2
3 3 3
4 4 4 4
5 5 5 5 5
6 6 6 6 6 6

"""
# =============================================================================================================
# n=4
# for i in range(1,n+1):
#     for j in range(1,n+2-i):
#         print(j,end=" ")
#     print("")

# output

"""
1 2 3 4 
1 2 3 
1 2 
1

"""

# =============================================================================================================
# n=4
# for i in range(1,n+1):
#     for j in range(1,n+1-i):
#         print(" ",end=" ")
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print("")
# output

"""
      1
    1 2
  1 2 3
1 2 3 4

"""

# =============================================================================================================
"""to find the last digit of the number and reverse the given number"""

# n=1234567
# while(n>0):
#   ld=n%10
#   print(ld)
#   n=n//10
  

# output
"""
7
6
5
4
3
2
1

"""

# =============================================================================================================
""" to find the first digit of the given number"""
# n=87654456
# while(n>0):
#     last_digit=n%10
#     n=n//10
#     if n==0:
#         print("the first digit is:",last_digit)
# output
"""the first digit is: 8 """

# =============================================================================================================
""" To find the count of the given number:"""
# n=56784532
# count=0
# while(n>0):
#     count+=1
#     n=n//10
# print("the count of this given number is:",count)

# output
"""the count of this given number is: 8 """

# =============================================================================================================
""" To find the number of odd digits in the given number"""
# n=2318329948311
# count=0
# while(n>0):
#     last_digit=n%10
#     if last_digit%2!=0:
#         count=count+1
#     n=n//10
# print("the count of the odd number is:",count)

# output
"""the count of the odd number is: 8 """
# =============================================================================================================

"""Given two numbers a and b, find kth digit from right of ab."""
# a=int(input("enter a number"))
# b=int(input("enter a number"))
# c=int(input("enter a number"))

# power=pow(a,b)

# count=0
# while(power>0):
#     count+=1
#     ld=power%10
#     if count==c:
#         print(ld)
#     power//=10


# example2 in method(function)

# def kthDigit( a, b, k):
#         power=pow(a,b)
#         count=0
#         while power>0:
#             count+=1
#             ld=power%10
#             if count==k:
#                 return ld
#             power//=10

# print(kthDigit(3,3,1))
    

# =============================================================================================================

"palindrome of the number"
# example 1
# n=11
# b=n
# sum=0
# while(n>0):
#     ld=n%10
#     sum=sum*10+ld
#     n//=10
# if sum==b:
#     print("palindrome")
# else:
#     print("not palindrome")



# example 2

# n=int(input("enter the number:"))
# d=str(n)
# pal=d[::-1]
# doc=int(pal)
# if n==doc:
    
#   print("it is a palindrome")
# else:
#   print("it is not a palindrome")

# output:

"""enter the number:123321
it is a palindrome """

# =============================================================================================================

"to print reverse of the number"
# example 1

# n=12345
# while(n>0):
#     ld=n%10
#     print(ld,end="")
#     n//=10


# example 2

# n=12345
# sum=0
# while(n>0):
#     ld=n%10
#     sum=sum*10+ld
#     n//=10
# print(sum)

# output

" 54321 "

# =============================================================================================================

" to find the factorial of the number"

# n=int(input("enter the number:"))
# fact=1
# for i in range(1,n+1):
#   fact=fact*i
# print(f"The factorial of {n} is :{fact}")

# output

""" 
enter the number:5
The factorial of5 is :120

"""

# =============================================================================================================
"to check the number is prime or not "


# def prime(n):
    
#   if n<=1:
#     return False
#   for i in range(2,int(n**0.5)+1):
#     if n%i==0:
#       return False
  
#   return True
  
# print(prime(3))

# outout:
"True "


# def prime(num1,num2):
#     for num in range(num1,num2+1):
#         if num>1:
#             for i in range(2,int(num**0.5)+1):
#                 if num%i==0:
#                     break
#             else:
#                 print(num,end=" ")
# prime(1,10)

# outout:
"2 3 5 7 "


# def prime(n):
#     for num in range(2,n+1):
#         check=True
#         for i in range(2,int(num**0.5)+1):
#             if num%i==0:
#                 check = False
#                 break
#         else:
#             print(num,end=" ")
# prime(20)
            
# outout:
" 2 3 5 7 11 13 17 19 "

# =============================================================================================================

"""
Given an integer n, find the number of divisors of n that are divisible by 3.

Examples:

Input: n = 6
Output: 2
Explanation: 1, 2, 3, 6 are divisors of 6 out of which 3 and 6 are divisible by 3.

"""
# n=15
# count=0
# for i in range(1,n+1):
#     if n%i==0:
        
#         if i%3==0:
            
#           count=count+1
# print(count)

# output:
" 2 "

# =============================================================================================================
"to find the trailing zeros of the factorial"
"explanation: 5!=120. the number of zeros in the end of the factorial is 1."

# brute force program

# n=12
# fact=1
# count=0
# for i in range(1,n+1):
#     fact=fact*i
# while(fact>0):
#     ld=fact%10
#     if ld==0:
#         count=count+1
#     else:
#         break
#     fact//=10
# print(count)


# optimized program

# n = 12
# count = 0
# i = 5
# while n // i > 0:
#     count += n // i
#     i *= 5
# print(count)

# output;
"2"

# =============================================================================================================
"To find the GCD of the two numbers"


# def gcd(a,b):
#     if a>=b:
#       gcd_value=1
#       for i in range(2,a+1):
#           if a%i==0 and b%i==0:
#               gcd_value=i
#       return gcd_value
#     elif b>a:
#       gcd_value=1
#       for i in range(2,b+1):
#           if a%i==0 and b%i==0:
#               gcd_value=i
#       return gcd_value
# a=int(input("Enter the number:"))
# b=int(input("Enter the number:"))
# print("the gcd of these number is ",gcd(a,b))

# output
"""
Enter the number:15
Enter the number:25
the gcd of these number is  5
"""

# =============================================================================================================
"to find the middle value of the given numbers"

# example 1

# def middle(a,b,c):
#     nums=[a,b,c]
#     sorted_num=sorted(nums)
#     mid_value=sorted_num[1]
#     return mid_value
# a=int(input("Enter a number:"))
# b=int(input("Enter a number:"))
# c=int(input("Enter a number:"))
# print(f"the middle value is:{middle(a,b,c)}")

# output

"""
Enter a number:500
Enter a number:600
Enter a number:100
the middle value is:500

"""
# example 2

# def mid(a,b,c):
#     if a>b and a>c:
#         return b if b>c else c
#     elif b>a and b>c:
#         return a if a>c else c
#     elif c>a and c>b:
#         return b if b>a else a
# print(mid(100,299,500))


# =============================================================================================================

"""Given the value of n, we need to find the sum of the series where i-th term is sum of first i natural numbers.

NOTE: Sum of the series 1 + (1+2) + (1+2+3) + (1+2+3+4) + …… + (1+2+3+4+…+n)

Example 1:

Input: n = 5
Output: 35 
Explanation: 1 + (1+2) + (1+2+3).. = 35
Hence sum of the series is 35."""

# n=7
# count=0
# sum=0
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         count=j+count
#     sum=count+sum
#     count=0
# print(sum)

# output

" 84 "

# optimized program

# def sumOfTheSeries (n):
     
#       return (n * (n + 1) * (n + 2)) // 6 
# print(sumOfTheSeries(7))

# =============================================================================================================

"""Given an integer n, your task is to compute the sum of all natural numbers from 1 to n (inclusive). If n is 0, the sum should be 0.

Examples:

Input: n = 3
Output: 6
Explanation: For n = 3, the sum will be 6. 1 + 2 + 3 = 6."""

# n=3
# sum=0
# for i in range(1,n+1):
#     sum=sum+i
# print(sum)

# optimized program

# def findSum( n):
#   return n*(n+1)//2

# output
"6"

# =============================================================================================================
"""Given an integer n, calculate the sum of series 13 + 23 + 33 + 43 + … till n-th term.

Examples:

Input: n = 5
Output: 225
Explanation: 13 + 23 + 33 + 43 + 53 = 225 --> 1 pow 3,2 pow 3, 3 pow 3 ...""" 

# n=7
# sum=0
# for i in range(1,n+1):
#     power=pow(i,3)
#     sum=sum+power
# print(sum)

# output
"784"

# optimized program

# def sumOfSeries( n):
#   return ((n * (n + 1)) // 2) ** 2

# =============================================================================================================

"""Given an integer N, find the absolute difference between sum of the squares of first N natural numbers and square of sum of first N natural numbers.

Example 1:

Input: N = 2
Output: 4 
Explanation: abs|(1**2 + 2**2) - (1 + 2)**2| = 4."""

# n=3
# count=0
# sum=0

# for i in range(1,n+1):
#     power=pow(i,2)
#     sum=sum+power

# for j in range(1,n+1):
#     count=count+j
# count_power=pow(count,2)

# print(abs(sum-count_power))

# output
" 22 "

# optimized program

# def squaresDiff (N):
#         sum_of_squares = (N * (N + 1) * (2 * N + 1)) // 6
#         square_of_sum = ((N * (N + 1)) // 2) ** 2
#         return abs(sum_of_squares - square_of_sum) 

# =============================================================================================================

