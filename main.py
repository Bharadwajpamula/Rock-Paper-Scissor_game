import random
choice={"rock":1,"paper":0,"scissor":-1}
computer=random.choice(list(choice.keys()))
yourChoice=input("enter your choice(rock,paper,scissor): ").lower()
if yourChoice not in choice:
    print("enter valid choice (rock,paper,scissor)")
else:
    computer_value=choice[computer]
    your_value=choice[yourChoice]

    print(f"you choosed {yourChoice}")
    print(f"computer choosed {computer}")

    if(your_value==computer_value):
        print("So, it's a Tie!")
    elif (your_value==1 and computer_value==-1) or \
        (your_value==0 and computer_value==1) or \
        (your_value==-1 and computer_value==0):
        print("Hurray! You Win!")
    else:
        print("Ouch! You Lost!")