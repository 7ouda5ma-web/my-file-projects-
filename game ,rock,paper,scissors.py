import random
rock=("👊")
paper=("🖐")
scissors=("✌")
print("welcome to the rock paper scissors game")
enter=input("press Enter to continue or type (Help) for the rules").capitalize()
if enter=="Help":
    print("""
           *********************RULES******************
           1).you choose and the computer chooses
           2).rock smashes scissors-> rock wins
           3).scissors cuts paper-> scissors wins
           4).paper covers rock-> paper wins
    """)
choice=input("enter your choice (rock,paper,scissors)\n").lower() 
if choice not in ["rock","paper","scissors"]:
    print("invalid choice")
    print("please enter rock,paper or scissors")
else :
    if choice=="rock":
        print("you choose rock\n",rock)
    elif choice=="paper":
        print("you choose paper\n",paper)
    else:
        print("you chose scissors\n",scissors)
    computer=random.choice(["rock","paper","scissors"])
    if computer=="rock":
         print("computer chose rock\n",rock)
    elif computer=="paper":
         print("computer chose paper\n",paper)
    else :
        print("computer chose scissors\n",scissors)
        if choice==computer:
            print("it 's a tie")
        elif (
            (choice=="rock" and computer=="scissors")
            or 
            (choice=="scissors" and computer=="paper")
            or
            (choice=="paper" and computer=="rock")
            ):
            print("you win")
        else:
            print("you lose")