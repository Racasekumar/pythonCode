# from collections import OrderedDict
# def check(s,string):
#     d=OrderedDict.fromkeys(s)
#     ind=0
#     for k,v in d.items():
#         if (k==string[ind]):
#             ind +=1
#         if (ind==len(string)):
#
#             return True
#     return False
#
#
#
# s=input()
# string=input()
# print(check(s,string))

# from collections import Counter
# def Check(a,b,c):
#     d1=Counter(a)
#     d2=Counter(b)
#     d3=Counter(c)
#
#     result=dict(d1 & d2 & d3)
#     for k,v in result.items():
#         print(k,v)
#
#
#
# a=[1,2,3,4,5,6,7,2,6,5,8]
# b=[4,5,8,3,2,9,4,2,5,8]
# c=[4,7,5,9,8,1,3,9,8]
# a.sort()
# b.sort()
# c.sort()
# print(Check(a,b,c))

# from collections import Counter
# def check(a,b,c):
#     d1=Counter(a)
#     d2=Counter(b)
#     d3=Counter(c)
#     d=dict(d1 & d2 & d3)
#     for k,v in d.items():
#         print(k)
#
#
#
#
#
# a=[1,2,3,4,3,4,5,6,7,8,8,9,7]
# b=[2,5,4,6,7,7,5,5,3,3,3,4,4,5]
# c=[4,5,6,3,2,4,5,6,7,6,5,4]
# a.sort()
# b.sort()
# c.sort()
# print(check(a,b,c))

# s=input()
# rotate=int(input())
# print(s)
# print(s[rotate:]+s[0:rotate])
# print(s[len(s)-rotate:]+s[0:len(s)-1])

# s=input()
# rotate=int(input())
# print(s)
# print(s[rotate:]+s[0:rotate])
# print(s[len(s)-rotate:]+s[0:len(s)-rotate])

# s=input()
# d={}
# for i in s:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
# print(d)

# from collections import Counter
# s=input()
# d=dict(Counter(s))
# for k,v in d.items():
#     if (v>1):
#         print(k)

# from collections import Counter
# s=input()
# d=dict(Counter(s))
# print(d)
# for k,v in d.items():
#     if (v>1):
#         print(k)

# import string
# ch=input()
# alpha=string.ascii_letters
# digit=string.digits
# pun=string.punctuation
# if ch in alpha or ch in digit or ch in pun:
#
#     print("not a special")
#
# else:
#     print("special")


# s=input()
# k=int(input())
# lst=s.split()
# for i in lst:
#     if (len(i)>k):
#         print(i)

# s=input()
# lst=s.split()
# k=int(input())
# for i in lst:
#     if (len(i)> k):
#         print(i)

# s=input()
# lst=s.split()
# print("-".join(lst))


# s=input()
# l=list(s.split())
# l.sort()
# for i in l:
#     print(i)

# s=input()
# vwl="aeiouAEIOU"
# count=0
# for ch in s:
#     if (ch in vwl):
#         count+=1
# print(count)

# s=input()
# l=list(s.split())
# print(" ".join(reversed(l)))


# class Solution:
#     def reverseVowel(self,s:str):
#     stack=[]
#     vwl="aeiouAEIOU"
#     res=""
#     for i in s:
#         if i.lower() in vwl:
#             stack.append(i)
#     for i in s:
#         if i in vwl:
#             res+=stack.pop()
#         else:
#             res+=i
#     return res

# s=input()
# s=list(s)
# vwl="aeiouAEIOU"
# i=0
# j=len(s)-1
# while i < j:
#     if s[i] in vwl and s[j] in vwl:
#         s[i],s[j]=s[j],s[i]
#         i+=1
#         j-=1
#     else:
#         if s[i] not in vwl:
#             i+=1
#         if s[j] not in vwl:
#             j-=1
# print("".join(s))

# s=input()
# s=list(s)
# vwl="aeiouAEIOU"
# i=0
# j=len(s)-1
# while i<j:
#     if s[i] in vwl and s[j] in vwl:
#         s[i],s[j]=s[j],s[i]
#         i+=1
#         j-=1
#     else:
#         if s[i] not in vwl:
#             i+=1
#         if s[j] not in vwl:
#             j-=1
# print("".join(s))


# from collections import Counter
# l=[4,3,2,7,8,2,3,1]
# d=dict(Counter(l))
# print(d)
# for k,v in d.items():
#     if v>1:
#         print(",".join(k))

# l=[4,3,2,7,8,2,3,1]
# d=[]
# for ele in l:
#     if l.count(ele)>1 and ele not in d:
#
#         d.append(ele)
# print(sorted(d))

# l=[4,3,2,7,8,2,3,1]
# d=[]
# for ele in l:
#     if l.count(ele)>1 and ele not in d:
#         d.append(ele)
# print(sorted(d))


def vwl(s):
    vwl=["a","e","i","o",U]













































