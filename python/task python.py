#GCD
a=0
b=20
graterst_common_divisor=0
if a !=0 and b!=0:
    for i in range(1,min(a,b)+1):
        if (a%i==0) and (b%i==0):
            graterst_common_divisor=i
elif a==0:
    graterst_common_divisor=b
elif b==0:
    graterst_common_divisor=a
print(graterst_common_divisor)

#sum of prime Numbers
n=20
sum_prime_numbers=0
for i in range(2,n+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        sum_prime_numbers+=i
print(sum_prime_numbers)

#sum of odd numbers
sum=0
for i in range(1,6):
    if i%2 !=0:
        sum+=i
print(sum)

#prime number

# num=2
# total=0
# count=0
# while count<20:
#     for i in range(2,num):
#         if num%i:
#             break
#     else:
#         total+=i
#         count+=1
#     num+=1
# print(total)

#perfect number
num=28
sum=0
for i in range(1,num):
    if num%i==0:
        sum+=i
if num==sum:
    print(f"it is perfect number{num}=={sum}")
else:
    print(f"Not perfect number {num}!={sum}")

#LCM
n1 = 12
n2 = 18
g = max(n1, n2)
for i in range(g, (n1 * n2) + 1, g):
    if i % n1 == 0 and i % n2 == 0:
        lcm = i
        break 
print(f"LCM of {n1} and {n2} is {lcm}")






    




