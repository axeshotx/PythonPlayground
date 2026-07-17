# 👉🏻1. Comp 2 int

# a = int(input("Enter first no."))
# b = int(input("Enter second no."))

# if a>b:
#     print(f"First num: {a} is greater")
# elif a<b:
#     print(f"Second num: {b} is greater")
# else:
#     print(f" {a} & {b} are equal ")

# 👉🏻2. & 3 Greet .... case sensitive

# a = input("Enter Your Gender (m/f) :- ")

# if a.upper() == "M":
#     print ("Hello Sir! How are you")
# elif a.upper() == "F":
#     print ("Hello Mam! How are you")
# else :
#     print ("Enter a valid input M/m or F/f only")

# 👉🏻4. Even ODD

# a = int(input("Enter a no. :-"))


# if a%2==0:
#     print(f"{a} is Even")
# else:
#     print(f"{a} is Odd")

# 👉🏻5. Vote

# n = input("What's Your Name:-")
# a = int(input(f"Hello {n}! Enter Your Age :- "))

# if a>=18:
#     print(f" Congrats {n} ! You can Vote and make a differece")
# elif a>102:
#     print(f"{n} ,Enter a Valid Age!")
# elif a<0:
#     print (f"{n} ,Enter your age not your marks.")
# else:
#     print(f"Chhotu {n} , {18-a} years until you can vote!")

# 👉🏻6. Number to day

# a = int(input("Enter a number from 1 to 7:-"))

# if a==1:
#     print("It's Monday!")
# elif a==2:
#     print("It's Tuesday!")
# elif a==3:
#     print("It's Wednesday!")
# elif a==4:
#     print("It's Thursday!")
# elif a==5:
#     print("It's Friday!")
# elif a==6:
#     print("It's Saturday!")
# elif a==7:
#     print("It's Sunday!")
# else:
#     print("Invalid! Learn to read and type from 1-7 only.")


# 👉🏻7. Greatest 3

# a = int(input("Enter 1st no. :-"))
# b = int(input("Enter 2nd no. :-"))
# c = int(input("Enter 3rd no. :-"))

# if c==b and a==c and b==a:
#     print("All three numbers are equal")
# elif a==b :
#     print(f"{a} and {b} are equal")
# elif a==c:
#     print(f"{a} and {c} are equal ")
# elif b==c:
#     print(f"{b} and {c} are equal ")
# if a!=b or b!=c or a!=c:   # Or helped me IKR!!
#     if a>=b and a>=c:  
#         print(f"1st num :- {a} is the greatest")
#     elif b>=a and b>=c:
#         print(f"2nd num :- {b} is the greatest")
#     elif c>=a and c>=b:     # Without >= [>] was making the condition false when any two no.s were equal thats why it wasn't working. 
#         print(f"3rd num :- {c} is the greatest")

# 👉🏻8. Leap Yr

# year = int(input("Enter a year (eg 2020) :- "))

# if year%400==0:
#     print(f"{year} is a leap year.")
# elif year%100!=0 and year%4==0:
#     print(f"{year} is a leap year.")
# else:
#     print("Not a leap year.")


# 👉🏻9. Discount

# amount= int(input("Enter your purchase amount:- "))

# if 999<amount<5000:                   # Here was the issue bruhhhh >amount<
#     print (f"You got 10% off! pay {amount*90/100}")     
# elif amount>=5000:
#     print (f"You got 20% off! pay {amount*80/100}")    
# else:
#     print(f"No discount Gareeb, Pay {amount} or add items of {1000-amount} to avail 10% off offer")


# 👉🏻10. Vowel

str = input("Enter an English alphabet:- ")

if str.lower()=="a" or str.lower()=="e" or str.lower()=="i" or str.lower()=="o" or str.lower()=="u":
    print("It's a vowel")
else:
    print("It's a consonant")



