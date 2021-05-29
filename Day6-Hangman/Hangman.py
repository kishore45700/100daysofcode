import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list=["camel","peacock","crow","cow","donkey"]
random_word=random.choice(word_list)
life=0
arr=[]
for i in range(0,len(random_word)):
    arr.append("_")
def check():
    for i in range(0,len(random_word)):
        if(arr[i]=="_"):
            return 0
    return 1
while(not check() and life<7):
    guess=input("Enter a letter : ")
    temp=0
    for i in range(0,len(random_word)):
        if(random_word[i]==guess):
            arr[i]=random_word[i]
            temp=1
    print(arr)
    if temp==0:
        print(stages[life])
        life+=1
        
            
            
    
