# 👉🏻 1. Hello World inp time
# '''
# str = int(input("Enter a no. :-"))

# # print ("Hello World\n"*str)

# for i in range(str):
#     print(f"Hello World! X{i+1}")
# '''

# 👉🏻 2. print till n 

# n = int(input("Enter a no. :-"))
# # for i in range(n):
# #     print(i+1)  

# or 

# for i in range(1,n+1):
#     print(i)

# 👉🏻 3. inp to 1

# n = int(input("Enter a no. :-"))

# for i in range (n,0,-1):
#     print(i)


# 👉🏻 4. Sum 1 to inp


# sum=0
# n = int(input("Enter a no. :-"))

# for i in range (1,n+1):
#     sum+=i
# print(sum)

# 👉🏻 5. factorial of inp

# f=1
# n = int(input("Enter a no. :-"))

# for i in range(n,1,-1):
#     f*=i                             #    print(f"Factorial of {n} is {i*(i-1)}")
    
# print (f)

# 👉🏻 6. Even odd sum till inp

# odd= 0
# even = 0
# a =int(input("Enter a No. Range :-"))

# for i in range (1,a+1):
#     if i%2==0:
#         even+=i    # not a cause it will add lets say start num 5 each time
#     else:
#         odd+=i

# print(f"Sum of Even no. = {even}")
# print(f"Sum of Odd no. = {odd}")

# 👉🏻 7. factors

# factor = "" ------ nope
# num =int(input("Enter the no. to find it's factors :-"))
# fact= 0
# for i in range(1,num+1):  # without 1 start it will give error , 0 div error
#     if num%i==0:
#         print(i)
#         fact+=1
# print(f"Total factors = {fact} ")


# 👉🏻 . 8 Factors sum

# fact = 0
# num =int(input("Enter the no. to find it's factors' sum :-"))

# for i in range (1,num+1):
#     if num%i==0:
#         fact+=i
        
# print(f"Sum of factors of {num} = {fact} ")

# 👉🏻 9. Power without **

# a = int(input("Enter base:- "))
# b = int(input("Enter power:- "))
# p=1

# for i in range (b):
#     p*=a
# print(f"{a}^{b} = {p}")




# 👉🏻 10. Prime no.

# a = int(input("Enter a no. :- "))
# f= 0

# for i in range(1,a+1):
#     if a%i==0:
#         f+=1

# if f==1:
#     print("It's a unity no.")    
# elif a==0:
#     print("It's 0, neither prime nor composite")
# elif f==2:
#     print("It's a prime no.")
# else:
#     print("It's a composite no.")


# ==========




# Prime no inp to inp 

# num = int (input())
# num2 = int (input())
# f=0
# prim= ""

# for i in range(num+1,num2):
#     if i%1==0 and i%i==0 and i%2!=0 or i==2 and i%3!=0 or i==3 and i%5!=0 or i==5 and i%7!=0 or i==7:
#         prim = prim + str(i) + " "
#         f+=1

# if f>0:
#     print(prim)
# elif f==0:
#     print("No prime")  WRONGGGGGGGGGGGGGGGGGGGGGGGGG







# -------------

# num = int (input("sATRT"))
# num2 = int (input("End"))
# j=""


# for i in range(num,num2):
#     x=str(i)
#     j= j + x + " "


# print(j , end=" ")



# Prime 

# st = int (input())
# ed = int (input())
# count=0
# primes=""

# for i in range (st+1, ed):
#     if j<2:
#             continue
#     for j in range (2,i):
        

#         if i%j==0:
#             count+=1
#     if count


inp = input()
low=0
cap=0

for i in inp:
    if i.islower()==True:
        low+=1
    elif i.isupper()==True:
        cap+=1

print(f"Uppercase: {cap}\nLowercase: {low}")


