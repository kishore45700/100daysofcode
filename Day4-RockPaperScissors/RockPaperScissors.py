import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

ch = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors.\n"))

com = random.randint(0,2)

if ch==0:
    print("You :\n"+rock)
    if com==1:
        print("Computer: \n"+paper)
        print("You lose!!")
    elif com==2:
        print("Computer: \n"+scissors)
        print("You win!!")
    else:
        print("Computer: \n"+rock)
        print("Its draw")
elif ch==1:
    print("You :\n"+paper)
    if com==2:
        print("Computer: \n"+scissors)
        print("You lose!!")
    elif com==0:
        print("Computer: \n"+rock)
        print("You win!!")
    else:
        print("Computer: \n"+paper)
        print("Its draw")
elif ch==2:
    print("You :\n"+scissors)
    if com==0:
        print("Computer: \n"+rock)
        print("You lose!!")
    elif com==1:
        print("Computer: \n"+paper)
        print("You win!!")
    else:
        print("Computer: \n"+paper)
        print("Its draw")