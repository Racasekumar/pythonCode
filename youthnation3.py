# n=int(input())
# for i in range(1,11):
#     print(n*i)


# def fib(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)
# n=int(input())
# for i in range (0,n):
#
#     print(fib(i))

# def fact(n):
#     if n==1:
#         return 1
#     else:
#         return(n* fact(n-1))
# n=int(input())
# print(fact(n))

# from collections import OrderedDict
# def Check(s,pattern):
#     d=OrderedDict.fromkeys(s)
#     ind=0
#     for k,v in d.items():
#         if (k==pattern[ind]):
#             ind+=1
#         if (ind==len(pattern)):
#             return True
#     return False
# s="sipravaraku"
# pattern="pra"
# print(Check(s,pattern))


# from collections import OrderedDict
# def Check(s,pattern):
#     d=OrderedDict.formkeys(s)
#     ind=0
#     for k,v in d.items():
#         if (k==pattern[ind]):
#             ind+=1
#         if (ind==len(pattern)):
#             return True
#     return False
#
# s=input()
# pattern=input()
# print(Check(s,pattern))

from collections import OrderedDict
def check(s,pattern):
    d=OrderedDict.formkeys(s)
    ind=0
    for k,v in d.items():
        if (k==pattern[ind]):
            ind+=1
        if (ind==len(pattern)):
            return True
        return False
s=input()
pattern=input()
print(check(s,pattern))




























