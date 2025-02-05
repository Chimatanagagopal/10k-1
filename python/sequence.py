list=['chimata','naga','gopal',2,5,['simple','comp'],True]
print(len(list))
print(list[2])
print(list[5][-1])
print(len(list[5]))
k=list[5]
print(k)
print(k[0])
print(list[1:])
print(list[:1])
print(list[-1:])
list[6]=False
#list[7]=True
print(list)
print(list[1: :-1])
print(len(list[5][ : ]))

#tuple
t=(2,2,5,6,7)
print(type(t))
print(t)
#t[-1]='gopal'
#print(t)
print(t.index(2))
l=[1,2,3,9,5]
print(id(l[1]))
print(id(l[2]))
print(id(l[3]))
l1=[9,4,7,6,5]
print(id(l1[1]))
print(id(l1[2]))
print(id(l1[3]))
for i in range(0,100+1):
    print(i)
list2=[1,2,3,4,5]
for i in range(0,len(list2)):
    print(list2[i])
    








