print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name=name1+name2
true_count=name.lower().count("t")+name.lower().count("r")+name.lower().count("u")+name.lower().count("e")
love_count=name.lower().count("l")+name.lower().count("o")+name.lower().count("v")+name.lower().count("e")

result=str(true_count)+str(love_count)
result=int(result)
if(result<10 or result>90):
    print(f"Your score is {result}, you go together like coke and mentos")
elif(result>=40 and result<=50):
    print(f"Your score is {result}, you are alright together.")
else:
    print(f"Your score  is {result}")