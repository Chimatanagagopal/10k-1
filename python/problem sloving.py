# a=2
# b=4
# c=6
# print(max(a,b,c))

# if (a>b) and (a>c):
#     larest=a
# elif (b>c) and (b>a):
#     larest=b
# else:
#     larest=c
# print(larest)

# l=[1,3,4,5,99]
# k=0
# for i in l:
#     if i>k:
#         k=i
# print(k)
# print(type(2+3j))


# #sum of the digits
# test=list(input("enter a numbers"))
# b=0
# for i in test:
#     b+=int(i)
# print(b)


#reverse 
# r=list(str(721))
# b=r.reverse()
# print(b)

#factoral

# n=int(input("enter a number"))
# a=1
# for i in range(1,n+1):
#     a *=i
# print(a)

#middle character
# middle='Wonder'
# middle1=len(middle)
# b=middle1//2
# if middle1 % 2 == 0:
#     jk=middle[b-1 : b+1]
# else:
#     jk=middle[b]

# print(jk)

#first and middle number

# n=input("enter a number")
# g=''
# num=list(n)
# for i in num[1:-1]:
#     if (num[0]>i) and (num[-1]>i):
#         g='true'
#     else:
#         g='false'
# print(g)
# units=40
# bill=0
# if units<=50:
#     bill+=0
# elif(units<=100):
#     bill+=units*50
# elif units<=150:
#     bill+=units*100
# elif units<=201:
#     bill+=units*150
# print(bill)

# str='helloworld'
# str1='aeiou'
# b=''
# for i in str:
#     for j in str1:
#         if i==j:
#             b+=i
# print(b[::-1])

# str1='helloworld'
# b=''
# for i in str1[::-1]:
#     b+=i
# print(b)
# c=str1.reversed()
# print(c)
#reverse
# text = "Hello, World!"
# reversed_text = ""
# for char in text:
#     reversed_text = char + reversed_text
# print(reversed_text)
# num1=1672
# num2=str(1672)
# a=int((num2[-1]))
# b=int((num2[0]))
# for i in num2[1:-1]:
#     if int(i)>a and int(i)>b:
#         print("true")
#     else:
#         print("false")
# n=list(num2)
# n.reverse()
# print(n)

#middle number
# str="Wonder"
# length=len(str)
# length1=length//2
# if length%2==0:
#     str2=str[length1-1:length1+1]
# else:
#     str2=str[str[length1]]
# print(str2)


# list=[10,2,3,4,5]
# b=1
# for i in list:
#     if b<i:
#         b=i
# print(b)
# s='goopal'
# s1='aeiou'
# s4=''
# for i in s:
#     for j in s1:
#         if i==j:
#             s4=j+s4
# print(s4)
# b=s4[0]
# for i in s4:
#     if b==i:
#         b.remove(i) 
# print(b)
# str='madam'
# print(set(str))
# str1=list(str)
# b=[]
# for i in str1:
#     if i  not in b:
#         b.append(i)
# print(b)
# c=[]
# for i in str:
#     if str.count(i)==1:
#         c.append(i)
# print(c)
# str= 'JohnWick'
# upper_case=''
# lower_case=''
# for i in str:
#     if i .isupper():
#         upper_case+=i
#     else:
#         lower_case+=i
# print(upper_case+lower_case)


# length=len(g)
# l1=length//2
# f=''
# if length%2==0:
#     f=g[l1-1:l1+1]
# else:
#     f=g[l1]
# print(f)

# def laregest_number(a):
#     b=a[0]
#     for i in a:
#         if i>b:
#             b=i
#     return b
# s=laregest_number([2,3,4,5,734,67,90,1,2])
# d=[2,3,4,5,734,67,90,1,2]
# e=max(d)
# d.remove(e)
# print(max(d))
# def add(a):
#     b=0
#     for i in a:
#         b+=i
#     return b
# g=add([1,2,3,4])
# print(g)
# k=add([1,2,3,4,4])
# print(k)
# l=[1, 2, 2, 3, 4, 4, 5]

# list=[1,2,3,4,6]
# list2=[]
# list3=[]
# for i in list:
#     if i%2==0:
#         list2.append(i)
#     else:
#         list3.append(i)

# print('Even :',list2)
# print('odd :',list3)
        


# list=[1,2,3,4,5]
# b=0
# c=0
# for i in list:
#     if i%2==0:
#         b+=i
#     else:
#         c+=i
# print('even',b)
# print('odd',c)

# list=["abcd" , "efghi" , "ghifh" , "dskf" , "sdddfsdf"]
# list1=""
# for i in list:
#     list1+=i[0]
# print(list1)

# str="python"
# str1=''
# for i in str:
#     str1=i+str1
# print(str1)

# I= [1, 2, 2, 3, 4, 4, 5] 
# g=[]
# for i in I:
#     if i not in g:
#         g.append(i)
# print(g)
# str="hello world"
# str1="aeiou"
# b=""
# for i in str:
#  print("gopal")




# a=2
# # print(type(a))
# # print(type(str(a)))
# # print(type(list(a)))
# print(tuple(a))
# print()

# print(2 and 4)
# print(True and False) 
# print(0 and False) 
# print(5 and "")
# print(12 ^ 24)
# range(0,15)


# list=[1,2,4,5,6,8]
# for i in list[::-1]:
#  print(i)
# n=1
# while n<5:
#     print(n)
#     n+=1


# if condition:
#     statement
# else:
#     statememt
      
# a=26
# if a % 2== 0:
#     print("divisible by 2")
# else:
#     print("not divisible by 2")

import numpy as np
# a=np.array([[1,2,3], [3,  4,"hjkl"]])
# print(a,a.ndim)
# b=np.array(28)
# print(len(a))
# b=np.arange(1,22,2)
# print(b)
# print(b.dtype)
# print(np.eye(4,dtype=float))
# print(np.zeros((3,5),dtype='int'))
# print(np.ones((3,5)))
# print(np.full((3,5),10))
# x=[1,2,3]  
# print(np.diag(x))

# x=np.arange(1,17)
# print(x[::-1])
# print(x.flatten())
# n=x.reshape((4,4))
# print(n)
# v=n.ravel()
# print(v)
# x1=5
# x2=5
# np.shares_memory(x1, x2)
# print(id(x1))
# print(id(x2))
# x=np.arange(1,17)
# y=x.reshape(4,4)
# print(y[y>3])
# print(y.transpose())
# print("------------")
# print(y)


# '''yes=[23,56,78,99]
# b=yes[0]
# for i in yes:
#     if i>b:
#         b=i
# print(b)'''




# g="madam"
# k=""
# for i in g:
#     k=i+k
# if k==g:
#     print("Palidrome")
# else:
#     print("not palidrome")

# h="madam"
# k=""
# for i in h:
#     k=i+k
# if k==h:
#     print("Palidrome")
# else:
#     print("not palidrome")
l=[1,2,3,5,6,7]
for i in range(min(l),max(l)+1):
    if i not in l:
        print(i)
    









  







