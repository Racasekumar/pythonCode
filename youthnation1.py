# from collections import Counter
# l=[1,1,1,1,2,2,2,3,2,3,4,4,5,5,4,3,3,2,2,2,2,2]
# d=dict(Counter(l))
# print(d)

# s=input()
# d={}
# for i in s:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
# print(d)

# n=int(input())
# for i in range(2,n):
#     if n%i==0:
#         print("not prime")
#         break
#
# else:
#     print("prime")


# s=input()
# if s==s[::-1]:
#     print("palindrome")
# else:
#     print("not palindrome")

# def fib(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)
# s=int(input())
# for i in range(0,s):
#     print(fib(i))

# def fact(n):
#     if n==1:
#         return 1
#     else:
#         return (n * fact(n-1))
# input=int(input())
# print(fact(input))

# a=input()
# b=list(map(int,input().split()))
# c=list(map(int,input().split()))
# x=sorted(b)
# y=sorted(c,reverse=True)
# print(*(x+y))
#
# n=list(map(int,input().split()))
# new=[]
# for x in n:
#     new.append(int(x))
#
# if new[0]> new[1]>new[2]:
#
#
#     print(min(new))


# def digit(n):
#     lst=list(str(n))
#     result=[int(i) for i in lst]
#     return result
# n=int(input())
# l=digit(n)
# count=0
# for i in l:
#     if (n%i ==0):
#         count+=1
# if (count == len(str(n))):
#     print("accepted")
# else:
#     print("rejected")

# def digit_lst(n):
#     lst=list(str(n))
#     result=[int(i) for i in lst]
#     return result
# n=int(input())
# l=digit_lst(n)
# count=0
# for i in l:
#     if (n% i ==0):
#         count +=1
# if (count == len(str(n))):
#     print("accepted")
# else:
#     print("rejected")

# def Factor(n):
#     for i in range(1,n+1):
#         result=[]
#         if (n%i ==0):
#             result.append(i)
#         return result
#
# start=int(input())
# end=int(input())
# for i in range (start,end+1):
#     l=Factor(i)
#     if (len(l)%2!=0):
#         print(i)

# def multi(m,n):
#     if n==1:
#         return m:
#     else:
#         return m (n+1)
# m=int(input())
# print(multi(m))
















