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
# num=1
# for i in range(n):
#     for j in range(n):
#         print(num,end=" ")
#         num+=1
#     print("")

# output:
"""
1 2 3 4 5 
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25

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

# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if j<i:
#             print(i,end=" ")
#         else:
#             print(j,end=" ")
#     print("")

# output:

"""
1 2 3 4 5 
2 2 3 4 5
3 3 3 4 5
4 4 4 4 5
5 5 5 5 5

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
#     for j in range(1,2*i):
#         print("*",end=" ")
#     print("")
# for i in range(1,n):
#     for j in range(1,i+1):
#         print(" ",end=" ")
#     for j in range(1,(2*n)-(2*i)):
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

"""You are given an integer n. Your task is to reverse the digits, ensuring that the reversed number has no leading zeroes.

Examples:

Input: n = 122
Output: 221
Explanation: By reversing the digits of number, number will change into 221."""


# n=21465401200
# while (n>0):
#     ld=n%10
#     if ld>0:
#         val=str(n)
#         rev=val[::-1]
#         print(rev)
#         break
#     elif ld==0:
#         n=n//10
        
# output
" 210456412 "
    
# =============================================================================================================

"""Given a positive integer n, find the number of perfect squares that are less than n in the sample space of perfect squares. The sample space consists of all perfect squares starting from 1 (i.e., 1, 4, 9, 16, 25, …)

Examples :

Input: n = 9
Output: 2
Explanation: 1 and 4 are the only Perfect Squares less than 9. So, the Output is 2."""

# n=3
# count=0
# for i in range(1,n):
#         power=pow(i,2)
#         if power<n:
#             count+=1
#         else:
#             break
# print(count)


# // if n=0 --> if the zero is given as n value//

# def countSquares(n):
#       count=0
#       if n==0:
#           return -2147483648
#       for i in range(1,n):
#               power=pow(i,2)
#               if power<n:
#                   count+=1
#               else:
#                   break
#       return count
# print(countSquares(10))

# output

" 3 "

# =============================================================================================================
"to iterate the elements from the array"

# arr=[1,2,3,4,5,6,7,8]
# for i in range(0,len(arr)):
#     print(arr[i])

"""
1
2
3
4
5
6
7
8
"""

# =============================================================================================================

"to add the values in the array"

# arr=[1,2,3,4,5,6,7]
# sum=0
# for i in range(0,len(arr)):
#     sum=sum+arr[i]
# print(sum)

# output
" 28 "

# =============================================================================================================
"to find the count of even and odd numbers in an array"

# def count(arr):
#     even=0
#     odd=0
#     for i in range(0,len(arr)):
#         if arr[i]%2==0:
#             even+=1
#         else:
#             odd+=1
#     return odd,even
# print(*count(arr=[1,2,3,4,5,6,7,8,9]))

# //---> * removes the paranthesis and comma from the output value. (5,4)--> 5 4

# output
" 5 4 "

# =============================================================================================================
"to find the largest number in the array "

# arr=[3,2,3,56,78,2,96,96,96,4,5,6,100,7,0]
# large=arr[0]
# for i in range(0,len(arr)):
#     if arr[i]>=large:
#         large=arr[i]
    
# print(large)

# output
" 100 "

# using in built function

# def largest(self, arr):
#         return max(arr)


# optimized program

# def largest(self, arr):
   
#     large = arr[0]
#     for num in arr:  
#         if num > large:
#             large = num
#     return large

# =============================================================================================================

""" Given an array, arr[] of integers, your task is to return the smallest and second smallest element in the array. If the smallest and second smallest do not exist, return -1.

Examples:

Input: arr[] = [2, 4, 3, 5, 6]
Output: [2, 3] 
Explanation: 2 and 3 are respectively the smallest and second smallest elements in the array."""

# def small(arr):
#     out=[]
#     sort=sorted(arr)
#     first=sort[0]
#     sec=sort[1]
#     out.append(first)
#     out.append(sec)
#     return out
# print(small(arr=[1,0,2,0,5,4,7,3]))

# --> optimized program and passes all the test cases-->

# def minAnd2ndMin(arr):
#         out=[]
#         sort=sorted(arr)
#         first=sort[0]
#         sec=None
#         for i in sort:
#             if i != first:
#                 sec=i
#                 break
#         if sec is None:
#             return [-1]
#         out.append(first)
#         out.append(sec)
#         return out
# print(minAnd2ndMin(arr=[1,0,2,0,5,4,7,3]))

# output
"[0, 1]"

# =============================================================================================================
"""Given an array arr. Your task is to find the minimum and maximum elements in the array.

Note: Return a Pair that contains two elements the first one will be a minimum element and the second will be a maximum.

Examples:

Input: arr[] = [3, 2, 1, 56, 10000, 167]
Output: 1 10000
Explanation: minimum and maximum elements of array are 1 and 10000."""

# def get_min_max(arr):
#     output=[]
#     sort=sorted(arr)
#     min=sort[0]
#     rev=sort[::-1]
#     max=rev[0]

#     output.append(min)
#     output.append(max)
#     return output

# print(get_min_max(arr=[1,0,2,0,5,4,7,3]))

# output
"[0,7]"
# =============================================================================================================

"""You are given an array arr[], the task is to return a list elements of arr in alternate order (starting from index 0).

Examples:

Input: arr[] = [1, 2, 3, 4]
Output: 1 3
Explanation:
Take first element: 1
Skip second element: 2
Take third element: 3
Skip fourth element: 4"""

# for knowing how to iterate alternate values from an array

# arr=[1,0,2,0,5,4,7,3]
# for i in range(0,len(arr),2):
#     print(arr[i])

# --> program <--

# def getAlternates(arr):
#     output=[]
#     for i in range(0,len(arr),2):
#         output.append(arr[i])
#     return output

# print(getAlternates(arr=[1,0,2,0,5,4,7,3]))

# output
"[1, 2, 5, 7]"

# =============================================================================================================

"""Given an array, arr[] of n integers, and an integer element x, find whether element x is present in the array. Return the index of the first occurrence of x in the array, or -1 if it doesn't exist.

Examples:

Input: arr[] = [1, 2, 3, 4], x = 3
Output: 2
Explanation: For array [1, 2, 3, 4], the element to be searched is 3. Since 3 is present at index 2, the output is 2."""
# -->to return the index of the first occurrence <--

# def search(arr, x):
#   for i in range(0,len(arr)):
#       if arr[i]==x:
#           return i
#   return -1

# print("index:",search(arr=[1,0,2,0,5,4,7,3],x=4))
# output:
"index: 5"

# -->to return the index of the nth occurrence <--

# arr=[2,3,4,1,4,6,4,2,1]
# x=1
# index_value=-1
# for i in range(0,len(arr)):
#     if arr[i]==x:
#         index_value=i
# if index_value==-1:
#     print("-1")
# else:
#     print(index_value)

# output:
"index_value: 8"

# =============================================================================================================
"to find the product of maximum value in arr1 and minimum value in arr2"

# arr1=[2,3,4,1,4,6,4,2,1]
# arr2=[2,3,4,4,6,4,2,]
# maxi=max(arr1)
# mini=min(arr2)
# print(maxi*mini)

# output:
" 12 "

# =============================================================================================================
"to find the prime numbers--> using seive of eratosthenes"

# a=int(input("enter the starting number:"))
# n=int(input("enter the final number:"))
# k=int(input("enter the kth number:"))
# prime=[1]*(n+1)
# prime[0]=prime[1]=0

# for i in range(2,int(n**0.5)+1):
#     if prime[i]==1:
#         for j in range(i*i,n+1,i):
#             prime[j]=0
# prime_list=[]
# count=0
# sum=0
# for i in range(a,n+1):
#     if prime[i]==1:
#         count=count+1
#         sum=sum+i
#         prime_list.append(i)
# print(f"the prime numbers between {a} and {n} are :{prime_list}")
# print(f"the count of the prime numbers are :{count}") 
# print(f"the {k}-th prime number is: {prime_list[k-1]}")
# print(f"the sum of prime numbers between {a} and {n} is:{sum}")

# output:
"""enter the starting number:2
enter the final number:100
enter the kth number:10
the prime numbers between 2 and 100 are :[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
the count of the prime numbers are :25
the 10-th prime number is: 29
the sum of prime numbers between 2 and 100 is:1060"""
    
# =============================================================================================================
"introduction to recursion "

# def rec(n):
#     if n==0:
#         return
#     else:
#         rec(n-1)

#         print(n)
# rec(5)

# output:
"""
1
2
3
4
5
"""

# =============================================================================================================
"""-->how to solve recursive problems<--
      1. break the problem into smaller problems
      2. start building logic behind the smaller problem
      3. find the recursive step for the given problem
      4. find the base condition
      5. build the recursive tree """

# problems

"""You are given an integer n. You have  to print all numbers from 1 to n.
Note: You must use recursion only, and print all numbers from 1 to n in a single line, separated by spaces.

Examples:

Input: n = 10
Output: 1 2 3 4 5 6 7 8 9 10"""

# def sum(n):
#     if n==0:
#         return
#     else:
#         sum(n-1)
#         print(n,end=" ")
# sum(10)

# output:
"1 2 3 4 5 6 7 8 9 10"
# =============================================================================================================


"""Given a non-negative integer n, your task is to find the nth Fibonacci number.

The Fibonacci sequence is a sequence where the next term is the sum of the previous two terms.

The first two terms of the Fibonacci sequence are 0 followed by 1. The Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21

The Fibonacci sequence is defined as follows:

F(0) = 0
F(1) = 1
F(n) = F(n - 1) + F(n - 2) for n > 1
Examples :

Input: n = 5
Output: 5
Explanation: The 5th Fibonacci number is 5."""

# def fib(n):
#     if n==1:
#         return 1
#     elif n==0:
#         return 0
#     return fib(n-1)+fib(n-2)

# n=int(input("enter the number:"))
# print(fib(n))

# output:
" 5 "
    
# =============================================================================================================
"to count the number of zeros in a number using recursion"

# def count_zero(n):
#     if n==0:
#         return 1
#     if n<10:
#         return 0
#     last_digit=n%10
#     if last_digit==0:
#         return 1+count_zero(n//10)
#     else:
#         return count_zero(n//10)
# print(count_zero(5060203000))

# output:
" 6 "

# =============================================================================================================
"to count the numbers of digits in a number using recursion"

# def digits(n):
#     if n<10:
#         return 1
#     return 1+digits(n//10)
# print(digits(1084523487))

# output:
" 10 "

# =============================================================================================================
"to find the sum of digits using recursion"

# def sum(n):
#     if n<10:
#         return n
#     ld=n%10
#     return ld+sum(n//10)
# print(sum(34534))

# output:
" 19 "

# =============================================================================================================
"to print the values from the array using recursion"

# def count(arr,i):
#     n=len(arr)
#     if i>=n:
#         return
#     print(arr[i])
#     return count(arr,1+i)
# count(arr=[1,2,3,4],i=0)

# output:
"""
1
2
3
4
"""

# =============================================================================================================
" to find the index value of the target value in an array using recursion"

# def search(arr,i,target):
#     n=len(arr)
#     if i==n:
#         if target!=arr[i-1]:
#             return -1
#     if target ==arr[i]:
        
#         return i
#     return search(arr,i+1,target)
# print(search(arr=[1,2,3,4,5,6],i=0,target=3))

# output:
" 2 "

# =============================================================================================================
"to find the sum of values in an array using recursion"

# def sum(arr,i):
#     n=len(arr)
#     if i==n-1:
#         return arr[i]
#     elif n>1:
#         return arr[i]+sum(arr,i+1)
# print(sum(arr=[0,32,4,45,36,52],i=0))

# output:
" 169 "

# =============================================================================================================
"to check whether the array is sorted or not using recursion"
# def asc(arr,i):
#     n=len(arr)
#     if i==n-1:
#         return True
#     if arr[i]<arr[i+1]:
#         return asc(arr,i+1)
#     return False
# print(asc(arr=[0,101,200,302,304,500],i=0))

# output"
" True "

# =============================================================================================================
"to print the divisors of a number using recursion"

# def div(n,i):
#     if i==n:
#         print(n,end=" ")
#         return 
#     if n%i==0:
#         print(i,end=" ")
    
#     return div(n,i+1)
# div(50,1)

# output:
" 1 2 5 10 25 50 "


# =============================================================================================================

"to find the power of a number using recursion"
# n-->the base number, i-->the initializer, pow-->the power number

# def power(n,i,pow):
#     if pow==0:
#         return 1
#     if i==pow:
#         return n
#     return n*power(n,i+1,pow)
# print(power(4,1,3))

# output:
" 64 "

# =============================================================================================================
"sorting an array using bubble sort"

# arr=[1,2,3,596,99,234,6,3,1,0]
# for i in range(1,len(arr)):
#     for j in range(0,len(arr)-1):
#         if arr[j]>arr[j+1]:
#             arr[j],arr[j+1]=arr[j+1],arr[j]
#         if j>len(arr):
#             break

# print(arr)

# output:
"[0, 1, 1, 2, 3, 3, 6, 99, 234, 596]"

# =============================================================================================================

"to remove special characters from a string"

# import re
# arr="sa$hba*gsr$^"
# result=re.sub(r'[^a-zA-Z0-9]',"",arr)
# print(result)

# output:
"sahbagsr"

"removing special characters in a string without importing re"

# arr="sa$hba*gsr$^"
# for i in arr:
#     if i =="$" or i== "*" or i=="^":
#         arr.replace(i,"")
#     else:
#       print(i,end="")

# =============================================================================================================
"to remove duplicates in an array"

# arr=[1,2,3,4,5,3,2,1,5,1,2,3,4,5,6,7,5,7,6,8,7,8,6,9,8,7,10]
# result=[]
# for i in arr:
#     if i not in result:
#         result.append(i)
# print(result)

# output:
"[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"

# =============================================================================================================
"to count the vowels in a string"

# name="gouthaman ravi"
# count=0
# for i in name:
#     if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
#         count+=1
# print(count)

# output
" 6 "

# =============================================================================================================
#                                             ---> BINARY SEARCH ALGORITHM <---

"to get an element index using binary search"

# def sort(arr):
#   arr1=sorted(arr)
#   print(arr1)
#   high=len(arr1)-1
#   low=0
#   x=20
#   while(low<=high):
#       mid=(high+low)//2

#       if arr1[mid]==x:
#           return mid   
             
                 
#       elif arr1[mid]<x:
#           low=mid+1
#       elif arr1[mid]>x:
#           high=mid-1
#   return -1
      
          
# print(sort(arr=[398,232,433,22,13,8,9,2,1]))
        
# OUTPUT:
" 5 "

# =============================================================================================================

"to find the second largest value in an array"

# def sec_large(arr):
#     large=arr[0]
#     for i in range(1,len(arr)):
#       if arr[i]>large:
#         large=arr[i]
#     second=-1
#     for j in range(0,len(arr)):
#         if arr[j]>second and arr[j]!=large:
#           second=arr[j]
#     return second
        
# print(sec_large(arr=[100,5,3,4,2,55,12,66,43,78]))

# output:
" 78 "

# =============================================================================================================
#                                    ---> MERGE SORTING <--- [DIVIDE & CONQUER]

# def mergesort(arr):
#     if len(arr)>1:
#         middle=len(arr)//2
#         left=arr[:middle]
#         right=arr[middle:]
#         mergesort(left)
#         mergesort(right)

#         lp=0
#         rp=0
#         fp=0
#         while len(left)>lp and len(right)>rp:
#             if left[lp]<right[rp]:
#               arr[fp]=left[lp]
#               lp+=1
#             else:
#                 arr[fp]=right[rp]
#                 rp+=1
#             fp+=1
#         while len(left)>lp:
#             arr[fp]=left[lp]
#             lp+=1
#             fp+=1
#         while len(right)>rp:
#             arr[fp]=right[rp]
#             rp+=1
#             fp+=1
#     return arr
# arr=[90,242,123,547,45,32,1,56,6,44,32,55,90,0]
# print(mergesort(arr))

# output:

" [0, 1, 6, 32, 32, 44, 45, 55, 56, 90, 90, 123, 242, 547] "

# =============================================================================================================
"""You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
 """
#                                        ---> merging the arrays from the last element of the array <---
# program:

# def merge(nums1, m, nums2, n):

#     lp=m-1    #to denote the last element of the nums1
#     rp=n-1      #to denote the last element of the nums2
#     fp=m+n-1  
#     while lp>=0 and rp>=0:
#         if nums1[lp]>nums2[rp]:
#             nums1[fp]=nums1[lp]
#             lp-=1

#         else:
#             nums1[fp]=nums2[rp]
#             rp-=1
#         fp-=1
#     while rp>=0:
#             nums1[fp]=nums2[rp]
#             rp-=1
#             fp-=1
#     return nums1
        

# =============================================================================================================
                              # ---> sorting 0,1,2 using dutch national flag algorithm <---

"""Given an array arr[] containing only 0s, 1s, and 2s. Sort the array in ascending order.
Note: You need to solve this problem without utilizing the built-in sort function.

Examples:

Input: arr[] = [0, 1, 2, 0, 1, 2]
Output: [0, 0, 1, 1, 2, 2]
Explanation: 0s, 1s and 2s are segregated into ascending order."""


# def dutch(arr):
#     left=0
#     mid=0
#     right=len(arr)-1
#     while mid<=right:
#         if arr[mid]==1:
#             mid+=1
#         elif arr[mid]==0:
#             arr[left],arr[mid]=arr[mid],arr[left]
#             mid+=1
#             left+=1
#         elif arr[mid]==2:
#             arr[right],arr[mid]=arr[mid],arr[right]
#             right-=1
#     return arr

# print(dutch(arr=[1,1,0,2,1,0,2,0]))


# output:

"[0, 0, 0, 1, 1, 1, 2, 2]"

# =============================================================================================================

"""Given an array arr, rotate the array by one position in clockwise direction.

Examples:

Input: arr[] = [1, 2, 3, 4, 5]
Output: [5, 1, 2, 3, 4]
Explanation: If we rotate arr by one position in clockwise 5 come to the front and remaining those are shifted to the end."""

# arr=[1,2,3,4,5,4]
# temp=arr[-1]
# i=len(arr)-1
# while i>=1:
#     arr[i]=arr[i-1]
#     i-=1
# arr[0]=temp
# print(arr)

# output:
'[4, 1, 2, 3, 4, 5]'

# =============================================================================================================

#                                               ----> rotate array by k <----

"""Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]"""


# def rotate(arr,k):
#     n=len(arr)
#     b=[]
#     k=k%n    #Because rotating an array by its length n (or any multiple of n) brings it back to the same place.So we only need to rotate by the remainder when dividing k by n.
#     for i in range(n-k,n):
#         b.append(arr[i])
        
#     for i in range(0,n-k):
#         b.append(arr[i])
        
#     return b
# print(rotate(arr=[1,2,3,4,5,6,7],k=4))

# output:
'[4, 5, 6, 7, 1, 2, 3]'

# =============================================================================================================
"""Given an increasing sorted rotated array arr[] of distinct integers. The array is right-rotated k times. Find the value of k.
Let's suppose we have an array arr[] = [2, 4, 6, 9], if we rotate it by 2 times it will look like this:
After 1st Rotation : [9, 2, 4, 6]
After 2nd Rotation : [6, 9, 2, 4]

Examples:

Input: arr[] = [5, 1, 2, 3, 4]
Output: 1
Explanation: The given array is [5, 1, 2, 3, 4]. The original sorted array is [1, 2, 3, 4, 5]. We can see that the array was rotated 1 times to the right.
Input: arr = [1, 2, 3, 4, 5]
Output: 0
Explanation: The given array is not rotated."""

# def findKRotation( arr):
#     if arr==sorted(arr):
#         return 0
#     if  len(arr)==1:
#         return 0
#     maxi=max(arr)
#     for i in range(0,len(arr)-1):
#         if arr[i]==maxi:
#             index=i
#             break
#     count=0
#     for j in range(index+1,0,-1):
#         count+=1
#     return count

# print(findKRotation(arr=[5,7,9,1,2,3,4]))

# output
'3'

# =============================================================================================================
"""Given two arrays a[] and b[] of equal size, the task is to find whether the elements in the arrays are equal.
Two arrays are said to be equal if both contain the same set of elements, arrangements (or permutations) of elements may be different though.
Note: If there are repetitions, then counts of repeated elements must also be the same for two arrays to be equal.

Examples:

Input: a[] = [1, 2, 5, 4, 0], b[] = [2, 4, 5, 0, 1]
Output: true
Explanation: Both the array can be rearranged to [0,1,2,4,5]
Input: a[] = [1, 2, 5], b[] = [2, 4, 15]
Output: false
Explanation: a[] and b[] have only one common value."""


# def check(a,b):
#   sort_a=sorted(a)
#   sort_b=sorted(b)
#   print(sort_b)
#   if sort_a==sort_b:
#     return True
#   else:
#     return False

# a=[1,2,5,4,0]
# b=[2,4,5,0,1]
# print(check(a,b))

# output:
"True"

# =============================================================================================================

"""Given an array arr[], check whether it is sorted in non-decreasing order. Return true if it is sorted otherwise false.

Examples:

Input: arr[] = [10, 20, 30, 40, 50]
Output: true
Explanation: The given array is sorted.
Input: arr[] = [90, 80, 100, 70, 40, 30]
Output: false
Explanation: The given array is not sorted."""

# def sort(arr):
#   for i in range(1,len(arr)):
#     if arr[i]<arr[i-1]:
#       return False
#   return True
# print(sort(arr=[7,0,1,2,3,4,5,6]))

# output:
"False"

# =============================================================================================================

"""You are given an array arr[] of non-negative integers. You have to move all the zeros in the array to the right end while maintaining the relative order of the non-zero elements. The operation must be performed in place, meaning you should not use extra space for another array.

Examples:

Input: arr[] = [1, 2, 0, 4, 3, 0, 5, 0]
Output: [1, 2, 4, 3, 5, 0, 0, 0]
Explanation: There are three 0s that are moved to the end.
Input: arr[] = [10, 20, 30]
Output: [10, 20, 30]
Explanation: No change in array as there are no 0s."""

# def sort(arr):   #brute force
#     n=len(arr)
#     for i in range(n):
#         for j in range(0,n-i-1):
#             if arr[j]==0:
#                 arr[j],arr[j+1]=arr[j+1],arr[j]
#     return arr
# print(sort(arr=[0,0,8]))



# def sort(arr):  #optimized program
#     n=len(arr)
#     pointer=0
#     for i in range(n):
#         if arr[i]!=0:
#             arr[pointer]=arr[i]
#             pointer+=1
#     while pointer<n:
#         arr[pointer]=0
#         pointer+=1
#     return arr
# print(sort(arr=[1,0,20,3,0,4,0,5,0]))

# output:
'[1, 20, 3, 4, 5, 0, 0, 0, 0]'

# =============================================================================================================
"to remove duplicates from an array"

# arr1=[1,2,3,4,5,6,7,3,4,5,6]
# arr2=[]
# for i in range(len(arr1)):
#     if arr1[i] not in arr2:
#         arr2.append(arr1[i])
        
# print(arr2)

# arr1=[0,0,1,1,1,2,2,3,3,3,3,4,4,4,4,5,5,5]
# i=0
# while i<len(arr1)-1:
#     if arr1[i]==arr1[i+1]:
#         arr1.pop(i)
#     else:
#         i+=1
# print(arr1)


# optimzed program:

# arr=[0,0,1,1,2,2,2,3,3,4,4,4,4,5]
# result = []
# for num in arr:
#     if not result or result[-1] != num:  # check last inserted element
#         result.append(num)
# print(result) 




# =============================================================================================================
"to find the LCM of two values"

# def gcd(a,b):
#     if a>=b:
#         gcd_value=1
#         for i in range(2,a+1):
#             if a%i==0 and b%i==0:
#                 gcd_value=i
#         return gcd_value
#     else:
#         gcd_value=1
#         for i in range(2,b+1):
#             if a%i==0 and b%i==0:
#                 gcd_value=i
#         return gcd_value
# def lcm(a,b):
#     lcmres=(a*b)//gcd(a,b)
#     return lcmres

# print(gcd(8,4))
# print(lcm(8,4))
    
        
# =============================================================================================================
"""Given an unsorted array arr[ ] having both negative and positive integers. The task is to place all negative elements at the end of the array without changing the order of positive elements and negative elements.

Note: Don't return any array, just in-place on the array.

Examples:

Input : arr[] = [1, -1, 3, 2, -7, -5, 11, 6 ]
Output : [1, 3, 2, 11, 6, -1, -7, -5]
Explanation: By doing operations we separated the integers without changing the order.
Input : arr[] = [-5, 7, -3, -4, 9, 10, -1, 11]
Output : [7, 9, 10, 11, -5, -3, -4, -1]"""
 
    
# def move_neg(arr):
#     pos=[]
#     neg=[]
#     for i in arr:
#         if i >=0:
#             pos.append(i)
            
#         else:
#             neg.append(i)
        
#     for i in range(len(pos)):
#         arr[i]=pos[i]
#     for i in range(len(neg)):
#         arr[len(pos)+i]=neg[i]
#     return arr

# print(move_neg(arr=[1,6,2,-5,3,0,-3,-1,10]))

# output:
"[1, 6, 2, 3, 0, 10, -5, -3, -1]"

# =============================================================================================================
"""Given an sorted array arr[] of integers. Sort the array into a wave-like array(In Place). In other words, arrange the elements into a sequence such that arr[1] >= arr[2] <= arr[3] >= arr[4] <= arr[5] ..... and so on. If there are multiple solutions, find the lexicographically smallest one.

Note: The given array is sorted in ascending order, and modify the given array in-place without returning a new array.

Examples:

Input: arr[] = [1, 2, 3, 4, 5]
Output: [2, 1, 4, 3, 5]
Explanation: Array elements after sorting it in the waveform are 2, 1, 4, 3, 5.
Input: arr[] = [2, 4, 7, 8, 9, 10]
Output: [4, 2, 8, 7, 10, 9]
Explanation: Array elements after sorting it in the waveform are 4, 2, 8, 7, 10, 9."""

# arr=[1,2,3,4,5,6]
# odd=[]
# even=[]
# odd.append(arr[0])

# for i in range(1,len(arr)):
#     if i%2!=0:
#         even.append(arr[i])
        
#     else:
#         odd.append(arr[i])

# result=[]
# for i in range(max(len(odd),len(even))):
#     if i<len(even):
#         result.append(even[i])
#     if i<len(odd):
#         result.append(odd[i])

# for i in range(len(arr)):
#             arr[i]=result[i]
        
# print(arr)

# output:
"[2, 1, 4, 3, 6, 5]"

# simplified program

# arr=[1,2,3,4,5]
# n=len(arr)
# for i in range(0,n-1,2):
#     arr[i],arr[i+1]=arr[i+1],arr[i]
# print(arr)

# =============================================================================================================

"""Given an array of integers arr[]. You have to find the Inversion Count of the array. 
Note : Inversion count is the number of pairs of elements (i, j) such that i < j and arr[i] > arr[j].

Examples:

Input: arr[] = [2, 4, 1, 3, 5]
Output: 3
Explanation: The sequence 2, 4, 1, 3, 5 has three inversions (2, 1), (4, 1), (4, 3).
Input: arr[] = [2, 3, 4, 5, 6]
Output: 0
Explanation: As the sequence is already sorted so there is no inversion count."""

# ------->> brute force program, time complexity: O(n^2)

# arr=[7, 72 ,90, 21 ,60]
# n=len(arr)
# count=0
# for i in range(n-1):
#     for j in range(i+1,n):
#         if arr[i]>arr[j]:
#           count+=1
# print(count)

# output:
" 4 "

# =============================================================================================================
"""The Union of two arrays is a collection of all distinct elements present in either of the arrays. If an element appears more than once in one or both arrays, it should be included only once in the result.

Note: Elements of a[] and b[] are not necessarily distinct.
Note that, You can return the Union in any order but the driver code will print the result in sorted order only.

Examples:

Input: a[] = [1, 2, 3, 2, 1], b[] = [3, 2, 2, 3, 3, 2]
Output: [1, 2, 3]
Explanation: Union set of both the arrays will be 1, 2 and 3.
Input: a[] = [1, 2, 3], b[] = [4, 5, 6] 
Output: [1, 2, 3, 4, 5, 6]
Explanation: Union set of both the arrays will be 1, 2, 3, 4, 5 and 6."""
# a=[1,2,3,0,0,2,2,2,1]
# b=[4,5,6,7,8,4,2,1]
# c=[]
# d=[]
# result=[]
# for i in a:
#     if i not in c:
#         c.append(i)
# for i in b:
#     if i not in d:
#         d.append(i)
# for j in c:
#     result.append(j)
# for j in d:
#     if j not in result:
#         result.append(j)
# print(result)

# output:
"[1, 2, 3, 0, 4, 5, 6, 7, 8]"

# optimized program:

# a=[1,2,3,0,0,2,2,2,1]
# b=[4,5,6,7,8,4,10,11]

# print(list(set(a)|set(b)))

# =============================================================================================================

"""You are given two arrays a[] and b[], return the Union of both the arrays in any order.

The Union of two arrays is a collection of all distinct elements present in either of the arrays. If an element appears more than once in one or both arrays, it should be included only once in the result.

Note: Elements of a[] and b[] are not necessarily distinct.
Note that, You can return the Union in any order but the driver code will print the result in sorted order only.

Examples:

Input: a[] = [1, 2, 3, 2, 1], b[] = [3, 2, 2, 3, 3, 2]
Output: [1, 2, 3]
Explanation: Union set of both the arrays will be 1, 2 and 3.
Input: a[] = [1, 2, 3], b[] = [4, 5, 6] 
Output: [1, 2, 3, 4, 5, 6]
Explanation: Union set of both the arrays will be 1, 2, 3, 4, 5 and 6."""


# a=[1,2,3,0,0,2,2,2,1]
# b=[4,5,6,7,8,4,10,11,23,55,89,1,2,3]
# res=[]
# c=list(set(a))
# d=list(set(b))
# print(c)
# print(d)
# print(res)
# if len(c)<len(d):
#     for i in range(len(c)):
#         for j in range(len(d)):                        # BRUTE FORCE METHOD
#             if c[i]==d[j]:
#                 res.append(c[i])
                
# if len(d)<len(c):
#     for i in range(len(d)):
#         for j in range(len(c)):
#             if d[i]==c[j]:
#                 res.append(d[i])
# print(res)


# ---------->> OPTIMIZED PROGRAM

# a=[1,2,3,0,0,2,2,2,1]
# b=[4,5,6,7,8,4,10,11,23,55,89,1,2,3]
# print(list(set(a)&set(b)))


# a=[1]
# b=[0]
# res=list(set(a)&set(b))       #----------->> if there is no common values print or return 1
# if len(res)>1:
#     print(res)
# elif len(res)<=0:
#     print("1")

# =============================================================================================================
"""Given an array arr[] of size n, containing elements from the range 1 to n, and each element appears at most twice, return an array of all the integers that appears twice.

Note: You can return the elements in any order but the driver code will print them in sorted order.

Examples:

Input: arr[] = [2, 3, 1, 2, 3]
Output: [2, 3] 
Explanation: 2 and 3 occur more than once in the given array.
Input: arr[] = [3, 1, 2] 
Output: []
Explanation: There is no repeating element in the array, so the output is empty."""


# def findDuplicates(arr):
#     res1 = []
#     res2 = []
    
#     for i in arr:
#         if i == 0:  
#             return res2  # skip 0s completely
#         if i not in res1:
#             res1.append(i)
#         elif i not in res2:   # to avoid multiple same duplicates
#             res2.append(i)
#     return res2
# print(findDuplicates(arr=[1,2,2,3,4,4,5,6,6,7]))

# output:
"[2, 4, 6]"

# =============================================================================================================
"""You are given an array arr of positive integers. Your task is to find all the leaders in the array. An element is considered a leader if it is greater than or equal to all elements to its right. The rightmost element is always a leader.

Examples:

Input: arr = [16, 17, 4, 3, 5, 2]
Output: [17, 5, 2]
Explanation: Note that there is nothing greater on the right side of 17, 5 and, 2.

Input: arr = [10, 4, 2, 4, 1]
Output: [10, 4, 4, 1]
Explanation: Note that both of the 4s are in output, as to be a leader an equal element is also allowed on the right. side

Input: arr = [5, 10, 20, 40]
Output: [40]
Explanation: When an array is sorted in increasing order, only the rightmost element is leader.

Input: arr = [30, 10, 10, 5]
Output: [30, 10, 10, 5]
Explanation: When an array is sorted in non-increasing order, all elements are leaders."""

# arr=  [16, 17, 4, 3, 5, 2]
# res=[]
# large=arr[-1]
# res.append(arr[-1])

# for i in range(len(arr)-2,-1,-1):
#   if large<=arr[i]:
#       large=arr[i]
#       res.append(large) 
# res.reverse()
# print(res)


# /output:
"[17, 5, 2]"

# =============================================================================================================
# prime numbers practice:

# def exam(n,num,k):
#     prime=[1]*(n+1)
#     prime[0]=prime[1]=0
#     for i in range(2,int(n**0.5)+1):
#         if prime[i]==1:
#             for j in range(i*i,n+1,i):
#                 prime[j]=0
#     result=[]
#     count=0
#     sum=0
#     for i in range(num,n+1):
#         if prime[i]==1:
#             count+=1
#             sum=sum+i
#             result.append(i)
#     return result ,count, sum, result[k-1]   #--> result[k-1]-returns the expected prime number from the result
# print(exam(20,2,3))

# output:
"([2, 3, 5, 7, 11, 13, 17, 19], 8, 77, 5)"

# =============================================================================================================

"""  BASICS OF EXCEPTION HANDLING """

# try:
#     a=int(input("enter a number:"))
#     b=int(input("enter a number:"))
#     try:
#       c=a//b
#     except Exception as e:
#         print("cause",e)
#     else:
#         print("result:",c)
# except Exception as e:
#     print("caught:",type(e).__name__,"-",e)

# finally:
#     print("the program is over")
    
# =============================================================================================================
" to reverse a string "

# a="geeks"
# rev=a[::-1]
# print(rev)

# =============================================================================================================
"""Given two non-empty strings s1 and s2, consisting only of lowercase English letters, determine whether they are anagrams of each other or not.
Two strings are considered anagrams if they contain the same characters with exactly the same frequencies, regardless of their order.

Examples:

Input: s1 = "geeks" s2 = "kseeg"
Output: true 
Explanation: Both the string have same characters with same frequency. So, they are anagrams.
Input: s1 = "allergy", s2 = "allergyy" 
Output: false 
Explanation: Although the characters are mostly the same, s2 contains an extra 'y' character. Since the frequency of characters differs, the strings are not anagrams. """

# output:
# def areAnagrams( s1, s2):
#     s1=s1.replace(" ","").lower()
#     s2=s2.replace(" ","").lower()
#     sort1=sorted(s1)
#     sort2=sorted(s2)
#     if sort1==sort2:
#         return True
#     else:
#         return False
# print(areAnagrams("geeks","skeeg"))

# output:
" True "

# =============================================================================================================
"""Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

A shift on s consists of moving the leftmost character of s to the rightmost position.

For example, if s = "abcde", then it will be "bcdea" after one shift.
 

Example 1:

Input: s = "abcde", goal = "cdeab"
Output: true
Example 2:

Input: s = "abcde", goal = "abced"
Output: false"""

# def rotateString( s, goal):

#     if len(s)!=len(goal):
#         return False
#     return goal in (s+s)
# print(rotateString("abcde","cdeab"))

# output:
" True "

# =============================================================================================================

#                                       ----> ASCII CODE <----

# a='a'                      # to convert character to number
# print(ord(a[0]))

# b=78                       #to convert numbers to character
# print(chr(b))


# a="gouthaman"
# for i in a:
#     print(i,":",ord(i))
# output:
"""
g : 103
o : 111
u : 117
t : 116
h : 104
a : 97
m : 109
a : 97
n : 110
"""

# a="gouthaman"
# ascii_list=[ord(i) for i in a]     # storing ascii codes in a list
# print(ascii_list)

# output:
"[103, 111, 117, 116, 104, 97, 109, 97, 110]"


# =============================================================================================================

# arr=["apple","banana","muskmelon",'cat']
# arr.sort(key=len)                           # to sort the array  by size of the elements
# print(arr)

# =============================================================================================================
"""Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings."""

# def longestCommonPrefix( strs):
       
#         prefix=''
#         for char in zip(*strs):               #--> zip==> (('f', 'f', 'f'), ('l', 'l', 'l'), ('o', 'o', 'i'), ('w', 'w', 'g'))
#             if len(set(char))==1:
#                 prefix+=char[0]
#             else:
#                 break
#         return prefix

# print(longestCommonPrefix(strs = ["flower","flow","flight"]))

# output:
" fl "

# =============================================================================================================
"""Given a sorted array arr with possibly some duplicates, the task is to find the first and last occurrences of an element x in the given array.
Note: If the number x is not found in the array then return both the indices as -1.

Examples:

Input: arr[] = [1, 3, 5, 5, 5, 5, 67, 123, 125], x = 5
Output: [2, 5]
Explanation: First occurrence of 5 is at index 2 and last occurrence of 5 is at index 5
Input: arr[] = [1, 3, 5, 5, 5, 5, 7, 123, 125], x = 7
Output: [6, 6]
Explanation: First and last occurrence of 7 is at index 6
Input: arr[] = [1, 2, 3], x = 4
Output: [-1, -1]
Explanation: No occurrence of 4 in the array, so, output is [-1, -1]"""

# def samp(arr,x):
#     n=len(arr)
#     first=-1
#     last=-1
#     low=0
#     high=n-1
#     while low<=high:
#         mid=(high+low)//2
#         if arr[mid]==x:
#             first=mid
#             high=mid-1
#         elif arr[mid]<x:
#             low=mid+1
#         else:
#             high=mid-1
#     low=0
#     high=n-1
#     while low<=high:
#         mid=(high+low)//2
#         if arr[mid]==x:
#             last=mid
#             low=mid+1
#         elif arr[mid]<x:
#             low=mid+1
#         else:
#             high=mid-1
#     return first ,last
# print(list(samp(arr=[1, 3, 5, 5, 5, 5, 7,67, 123, 125],x=5)))

# output:
"[2, 5]"
        
# =============================================================================================================
"""You are given an array arr[] of size n - 1 that contains distinct integers in the range from 1 to n (inclusive). This array represents a permutation of the integers from 1 to n with one element missing. Your task is to identify and return the missing element.

Examples:

Input: arr[] = [1, 2, 3, 5]
Output: 4
Explanation: All the numbers from 1 to 5 are present except 4.
Input: arr[] = [8, 2, 4, 5, 3, 7, 1]
Output: 6
Explanation: All the numbers from 1 to 8 are present except 6.
Input: arr[] = [1]
Output: 2
Explanation: Only 1 is present so the missing element is 2."""

# def find(arr):

#     n = len(arr) + 1   # because array size is n-1
#     total_sum = n * (n + 1) // 2
#     arr_sum = sum(arr)
#     return total_sum - arr_sum
# print(find(arr=[8, 2, 4, 5, 3, 7, 1]))

# output:
" 6 "

# =============================================================================================================
"""Given a sorted array arr[]. Find the element that appears only once in the array. All other elements appear exactly twice. 

Examples:

Input: arr[] = [1, 1, 2, 2, 3, 3, 4, 50, 50, 65, 65]
Output: 4
Explanation: 4 is the only element that appears exactly once.
Input: arr[] = [5]
Output: 5
Input: arr[] = [1, 2, 2, 3, 3]
Output: 1"""

#                                           ---> solved using binary search <---

# def once(arr):
#     n=len(arr)-1
#     low=0
#     high=n
#     while low<high:
#         mid=(low+high)//2
#         if mid%2==1:
#             mid-=1
#         if arr[mid]==arr[mid+1]:
#             low=mid+2
#         else:
#             high=mid
#     return arr[low]
# print(once(arr=[1,1,2,2,3,3,4,6,6]))

# output:
" 4 "

# =============================================================================================================

"""Given a sorted and rotated array arr[] of distinct elements, the task is to find the index of a target key.  If the key is not present in the array, return -1.

Examples :

Input: arr[] = [5, 6, 7, 8, 9, 10, 1, 2, 3], key = 3
Output: 8
Explanation: 3 is found at index 8.
Input: arr[] = [3, 5, 1, 2], key = 6
Output: -1
Explanation: There is no element that has value 6.
Input: arr[] = [33, 42, 72, 99], key = 42
Output: 1
Explanation: 42 is found at index 1."""


# def search(arr,key):
#     low=0
#     high=len(arr)-1
#     while low<=high:
#         mid=(low+high)//2
#         if key==arr[mid]:
#             return mid
#         if arr[mid]>arr[low]:
#             if key>=arr[low] and arr[mid]>key:
#                 high=mid-1
#             else:
#                 low=mid+1
#         else:
#             if key>arr[mid] and arr[high]<=key:
#                 low=mid+1
#             else:
#                 high=mid-1
#     return -1

# print(search(arr=[5, 6, 7, 8, 9, 10, 1, 2, 3],key=3))

# output:
" 8 "

# =============================================================================================================
"""A sorted array of distinct elements arr[] is rotated at some unknown point, the task is to find the minimum element in it. 

Examples:

Input: arr[] = [5, 6, 1, 2, 3, 4]
Output: 1
Explanation: 1 is the minimum element in the array.
Input: arr[] = [3, 1, 2]
Output: 1
Explanation: Here 1 is the minimum element.
Input: arr[] = [4, 2, 3]
Output: 2
Explanation: Here 2 is the minimum element."""

# def findMin( arr):
#     low=0
#     high=len(arr)-1
#     while low<high:
#         mid=(low+high)//2
#         if arr[mid]>arr[high]:
#             low=mid+1
#         else:
#             high=mid
#     return arr[low]

# print(findMin(arr=[5,6,7,1,2,3,4]))

# output:
" 1 "

# =============================================================================================================
def largest(arr):
    low=0
    high=len(arr)-1
    while low<high:
        mid=(low+high+1)//2
        if arr[mid]>=arr[low]:
            low=mid
        else:
            high=mid-1
    return arr[low]
print(largest(arr=[5,6,7,1,2,3,4]))
