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
