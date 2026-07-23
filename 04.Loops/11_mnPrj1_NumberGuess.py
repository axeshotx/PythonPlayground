# Number guessing

import random

num= random.randint(1,100)

score = 10
x=10
trials =0

name = input("Enter Your Name here Player:- ")
print(f"Hello {name} 👋🏻 ! You have to guess a number from 1 to 100\n")
while True:

    a = int(input(f"Enter a no. to guess ({score} Chances Left) :- "))

    if score==0:
        print(f" 🙂 Better Guess next time {name}. 👉🏻 {num} was the number. ")
        break
    elif num==a:
        print(f"🎊 You got it , {name}'s Score : {score}")
        break
    elif a>num:
        print(f"👻 No! Guess a bit lower {name}\n")
        trials+=1
        score-=1
    elif a<num:
        print(f"👻 No! Guess a bit above {name}\n")
        trials+=1
        score-=1
        

