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


# upper lower counter

# inp = input()
# low=0
# cap=0

# for i in inp:
#     if i.islower()==True:
#         low+=1
#     elif i.isupper()==True:
#         cap+=1

# print(f"Uppercase: {cap}\nLowercase: {low}")

# odd and even digit count 


# write your code here

inp = input()
ev= 0
od= 0

for i in inp.strip():
    x=int(i)
    if x%2==0:
        ev+=1
    elif x%2==1:
        od+=1

print(f"Even: {ev}\nOdd: {od}")



