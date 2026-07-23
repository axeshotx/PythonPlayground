import random


score=0
botsc=0



name = input("Hey Player! Enter Your Name :- ")
print(f"Hello {name} 👋🏻 ! This is Stone Papers Scissors Against Me(Your Comp.) \n")

while True:
    print(f"Scores = 😎 {name} :- {score} | 🤖 Computer:- {botsc} \n ")
    user = int(input(f"Enter number 1-Stone or 2-Paper or 3-Scissors ({5-score} More Points to win) :- "))
    comp= random.randint(1,3)

    # if score==5 or botsc==5:   weird
    #     break


    if user==1 and comp ==3:
        print("You Won this round! \n")
        score+=1
    elif user==2 and comp==1:
        print("You Won this round! \n")
        score+=1
    elif user==3 and comp==2:
        print("You Won this round! \n")
        score+=1
    elif user==comp:
        print("It was a draw this round!")
    else:
        print("Computer won this round!")
        botsc+=1

    if score==5 or botsc==5:
        break
    # Comp code


if score ==5:
    print(f"Scores = 😎 {name} :- {score} | 🤖 Computer:- {botsc} \n ")
    print(f"🎊 Congrats {name} ! You Won!")

elif botsc ==5:
    print(f"Scores = 🤖 Computer:- {botsc} | 😎 {name} :- {score} \n ")
    print(f"👾 I won! Better Luck Next time {name} !")
























    # elif user==3 and comp==1:
    #     print("I Won this round! destroyed your Scissors this time\n")
    #     botsc+=1
    #     score-=1
    # elif user==1 and comp==2:
    #     print("I wrapped your Stone this time\n")
    #     botsc+=1
    #     score-=1
    # elif user==2 and comp==3:
    #     print("I tore your papers this time\n")
    #     botsc+=1
    #     score-=1