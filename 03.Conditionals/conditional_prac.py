# i = int(input())

# x= str(i)
# z =x[::-1]
# y= len(z)


# if z[0]=="0":
#     print(z[1:y+1])
# else:
#     print(z)
 

i = int(input().strip())

x= str(i)
z =x[::-1]

if x[0]=="-":
    print(f"-{z[::]}")



# str = input()
# lst= len(str)

# if lst%2==0:
#     x = lst//2
#     print(str[x-1])
# elif lst%2==1:
#     # lst+=1
#     x = lst//2
#     print(str[x])