# l=20
# b=30
# print('* '*b)
# for i in range(1,l-1):
#     print('*'+(' '*((b*2)-3))+'*')
# print("* "*b)   


# for i in range(10,0,-1):
#     str1=""
#     for j in range(1,i+1):
#          str1=str1+str(j)+" "
#     print(str1)


# for i in range(1,6):
#     str3=""
#     for j in range(1,i+1):
#         str3=str3+str(j)+" "
#     print(str3)

# n=6
# for i in range(1,n):
#     for j in range(1,i+1):
#         print(" ",end=" ")
#     for k in range(i,n):
#         print('*',end=" ")

#     print()
# n=6
# for i in range(n,0,-1):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for k in range(1,i+1):
#         print("*",end=" ")
#     for k in range(1,i):
#         print("*",end=" ")
    
#     print()
# n=4
# for i in range(n,0,-1):
#     for j in range(i,n):
#         print(' ',end=" ")
#     for i in range(1,i+1):
#             print('*',end=" ")
#     for k in range(1,i):
#         print('*',end=" ")
#     print()
# for i in range(0,n+1):
#     for j in range(i,n):
#         print(' ',end=" ")
#     for i in range(1,i+1):
#             print('*',end=" ")
#     for k in range(1,i):
#         print('*',end=" ")
#     print()

# n=5
# for i in range(1,n):
#     for j in range(1,i+1):
#         print('*',end=" ")
#     for w in range(i,n):
#         print(' ',end=" ")
#     for _ in range(i,n):
#         print(' ',end=" ")
#     for q in range(1,i+1):
#         print('*',end=" ")
#     print()
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print('*',end=" ")
#     for w in range(i,n):
#         print(' ',end=" ")
#     for _ in range(i,n):
#         print(' ',end=" ")
#     for q in range(1,i+1):
#         print('*',end=" ")
#     print()

#ASSIGRMET OPRATOR


a=20
# print(a)
#=,+=,-=,*=,**=
# a=a+20
# print(a)
# a+=20
# print(a)
# a-=10
# print(a)
# a/=2
# print(a)
#bitwise oprator
# &,|,^,~,>>,<<
# print(2 & 3)
# print(bin(2 | 3))

#relational oprator
# >,<,==,!=,>=,<=
# a=2
# b=3
# print(a>5)
# print(a<5)
# print(b<2)
# print(a==b)
# print(a!=b)
# print(a>=b)
# print(a<=b)
# a=input("enter your name")
#data types
#int
# # 1,3,4,5,6,7,8,8
# a=2
# print(type(a))
#float
2.3,66.7,88.55
#complex
#a+jb
# a=2+3
# b=3+2j
# print(a+b)
# #list
# list=[1,2,3,4,3.4,6.5,"apple"]

# list1=list((1,3,5))
# print(type(list1))
# a=2
# b=2
# c=354565
# print(id(a))
# print(id(b))
# print(id(c))
# for i in range(1,6):
#     for i in range(1,i+1):
#         print("*",end=" ")
#     print()
# a="somethimg"
# b=""
# c="aeiou"
# for i in a:
#     if i not in c:
#         b=b+i
# print(b)
# c=[]
# for i in b:
#     if b.count(i)==1:
#         c.append(i)
# print(str(c))




# #Butterfly Pattern
# print("Butterfly Pattern")
# n=5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     for k in range(i,n):
#         print(" ",end=" ")
#     for m in range(i,n):
#         print(" ",end=" ")
#     for r in range(1,i+1):
#         print("*",end=" ") 
#     print()
# for i in range(n-1,0,-1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     for k in range(i,n):
#         print(" ",end=" ")
#     for m in range(i,n):
#         print(" ",end=" ")
#     for r in range(1,i+1):
#         print("*",end=" ") 
#     print()


# #Diamond Pattern
# print("Diamond Pattern")
# n=5
# for i in range(1,n+1):
#     for j in range(i,n+1):
#         print(" ",end=" ")
#     for k in range(1,i+1):
#         print("*",end=" ")
#     for m in range(1,i):
#         print("*",end=" ")
#     print()
# n=5
# for i in range(n-1,0,-1):
#     for j in range(i,n+1):
#         print(" ",end=" ")
#     for k in range(1,i+1):
#         print("*",end=" ")
#     for m in range(1,i):
#         print("*",end=" ")
#     print()


# #Hourglass Pattern
# print("Hourglass Pattern")
# n=5
# for i in range(n,1,-1):
#     for j in range(i,n+1):
#         print(" ",end=" ")
#     for k in range(1,i+1):
#         print("*",end=" ")
#     for m in range(1,i):
#         print("*",end=" ")
#     print()
# for i in range(1,n+1):
#     for j in range(i,n+1):
#         print(" ",end=" ")
#     for k in range(1,i+1):
#         print("*",end=" ")
#     for m in range(1,i):
#         print("*",end=" ")
#     print()


# #Pyramid Pattern
# print("Pyramid Pattern")
# for i in range(1,n+1):
#     for j in range(i,n+1):
#         print(" ",end=" ")
#     for k in range(1,i+1):
#         print("*",end=" ")
#     for m in range(1,i):
#         print("*",end=" ")
#     print()


# #Square
# print("Square")
# l=4
# b=6
# print('* '*b)
# for i in range(1,l+1):
#     print('*'+' '*((2*b)-3)+'*')
# print('* '*b)

#list
# d=[1,2.3,"gopal",["usha" ,"rama",2,6],["wertt",2,88,5.7]]
# print(d)
# f=list((1,2.3,"gopal",2,4,5,66,1))
# print(f)
# print(d[-1])

# d[2]="gfhj"
# print(d)
# print(d[-1::0])
# print(d[3][1])
# d[3][0]="divya"
# print(d)

# print(d[-1])
# d[3][1],d[4][0]="qwew","oooo"
# print(d[3][1])
# d[4][2]
# print(d[4][3])
# print(d)

#string
# g=" hjbhgfds juhygtf"
# print(g[0])
# print(g[::-1])
# #tuple
# p=(1,3,2,77,0,"naga","gopal")
# print(type(p))
# print(p[-1])
# for rows in range(5,0,-1):
#     for j in range(1,rows+1):
#         print('*',end=" ")
#     print()
# def fun(first_name="naga",last_name="gopal",g):
#     print(first_name)
# fun("gopal","naga",g="")
# def add(a,b,g,c=9):
#     print(a+b+c+g)
# add(2,3,5)

#return
# '''hyujieokrijhugfhjkl'''
#return
# def fun(a):
#    d= "even" if a%2==0 else "odd"
#    print(d)           
# fun(2)
#set
# s1={2.4,6,7,8,"asdfghj",6}
# print(s1)
# # print(s1[-1])
# s1.add(123)
# print(s1)
# dict={"vinay":"anu","fruit":"apple","yuvaraj":"king","gfhjk":56,"vinay":"indhu",}
# print(dict["fruit"])
# dict["vinay"]="charitha"
# print(dict)
# for i in range(6):
#     for j in range(1,i+1):
#         print(" ",end=" ")
    
#     for i in range(i,6):
#         print("*",end=" ")
#     print()

# def some(a,b):
#     return a+b
# a=some(2,3)
# def some(a,b,c):
#     return a+b+c
# b=some(4,5,6)
# def some(a,b,c,d):
#     return a+b+c+d
# c=some(7,8,9,10)


# print(a)
# print(b)
# print(c)

# def sum(**d):
#     print(d)
# sum(name="gopal",name1="naga",int=33)



'''types of functions
viod functions
functions with return statements 
lambda x,y,z=x+y+z
'''
# a=lambda x,y,z:x+y+z ,1,2,35
# print()
# def add(**h):
#     print(h)
# add(num1=2,num2=3,num3=45,num4=6,num5=78,str="lkjhgfc")

# def add(a,b,c):
#     print(a)
# add(2,8,9)


# a=lambda a,b:a-b
# print(a(1,2))

# num1=20
# def fun():
#     print(num1)
#     global num1
#     num1=50
# fun()
# print(num1)
# def fun1():
#     print(g)
# fun1() 

# 
# a='qsdwefrgth'
# b=int(a)
# print(b,type(b))
# for i in range(1,5):
#     for j in range()
# l1=[1,2,3,4,5]
# l2=[2,3,4,5,7]
# b=" ".join(str(l1+l2))
# print(b)
a=2
# if a%2==0:
#     print("even")
# else:
#     print("odd")
# b="even" if a%2==0 else "odd"
# print(b)
# for i in  range(1,6):
#     for j in range(1,i+1):
#         print('*',end=" ")
#     for k in range(5,i,-1):
#         print(" ",end=" ")
#     for k in range(5,i,-1):
#         print(" ",end=" ")
#     for j in range(1,i):
#         print('*',end=" ")
#     print()
# for i in  range(5,0,-1):
#     for j in range(1,i+1):
#         print('*',end=" ")
#     for k in range(5,i,-1):
#         print(" ",end=" ")
#     for k in range(5,i,-1):
#         print(" ",end=" ")
#     for j in range(1,i+1):
#         print('*',end=" ")
#     print()


"""oops"""
# class gopal():
#     a=20
#     b=40
#     print("Hello","Gopal")
# p=gopal()
# p1=gopal()
# p1.a=67
# print(p1.a)
# print(p.a)

# class naga():
#     def sampleMethod(self):
#         print("asdf")
#         c=90
# n1=naga()
# n1.sampleMethod()

# class bank():
#     def __init__(self,an,ac,ic,b):
#         self.an=an
#         self.ac=ac
#         self.ic=ic
#         self.b=b
#     def display(self):
#         print(self.an,self.ac,self.ic,self.b)
# obj1=bank(12345,"fgyhuijop","ftgyhuijo",789)
# obj1.display()
# class inter():
#     b=70
#     def __init__(self,name,std):
#         self.name=name
#         self.std=std
# inter1=inter("gopal","btech")
# print(inter1.name)
# print(inter1.std)

# class A:
# 	def __init__(self,b):
# 		self.b=b

# obj=A("Hello")
# del obj

# class some():
#     def __init__(self,a,b):
#         self.a=a  
#         self.b=b
#     def add(self):
#         return self.a+self.b

# obj=some(2,4)
# print(obj.add() ) 

# class one():
#     def chepali(self):
#         print("vinay")
# class two(one):
#     def ga(self):
#         print("hero")
# class three(two):
#     def nuvvu(self):
#         print("indhu")
# obj=three()
# obj.chepali()
# obj.ga()

'''class Student:
    def __init__(self, name, age):
        self.name = name        # Public attribute
        self.__age = age        # Private attribute

    def get_age(self):          # Public method to access private attribute
        return self.__age

    def set_age(self, age):     # Public method to modify private attribute
        if age > 0:
            self.__age = age
        else:
            print("Age must be positive!")

# Creating an object
student = Student("Alice", 20)

# Accessing public attribute
print(student.name)  # Output: Alice

# Accessing private attribute (will cause an error)
# print(student.__age)  # AttributeError

# Using getter method to access private attribute
print(student.get_age())  # Output: 20

# Using setter method to modify private attribute
student.set_age(25)
print(student.get_age())  # Output: 25'''

# str="helloo"
# str1="aeiou"
# str2=""
# str3=""
# for i in str:
#     for j in  str1:
#         if i==j:
#             str2+=i
# print(str2)
# s="Gopal"
# l=""
# for char in s:
#     if char.isupper():
#         l+=char.lower()
#     else:
#         l+=char.upper()
# print(l)



rp=[9,1,2,3,5,6]
s=set(rp)
s1=list(s)
s1.sort()
print(s1)







    






















    

