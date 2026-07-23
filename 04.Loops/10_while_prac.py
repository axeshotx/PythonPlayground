# 1. 👉🏻 Print Reverse Digits sep. 

# num = int(input("Enter no. :- ").strip())

# while num>0:
#     print(num%10)
#     num = num//10

# 👉🏻 2 Digits sum of a number

# num = int(input("Enter no. :- ").strip())
# sum = 0

# while num>0:
#     # mod = num%10
#     sum += num%10
#     num = num//10

# print(sum)

# 👉🏻  3 Reverse no

# num = int(input("Enter :- "))
# rev = 0

# while num >0 :
#     rev = rev * 10 + num%10
#     num = num//10

# print(rev)

# 👉🏻  4 Palindrome check
# num = int(input("Enter :- "))
# num = abs(num)
# old = num
# rev = 0

# while num >0 :
#     rev = rev * 10 + num%10
#     num = num//10

# if old==rev:
#     print(f" {rev} is a Palindrome no.")
# else:
#     print(f"{old} is Not a palindrome")

# 👉🏻  5 Automorphic number

a = int(input("Enter:- "))
copy = a          # 625
sq = a**2
dg = 0


while a>0:
    dg+=1
    a=a//10

pal = sq%(10**dg)

if pal == copy:
    print("Automorphic no. ✅")
else:
    print("Not Automorphic no. ❌")

