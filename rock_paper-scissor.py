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
game_images=[rock, paper, scissors]
user_choise=int(input("What do you choose ? Type 0 for Rock, 1 for Paper, or 2 for Scissors .\n"))
print(game_images[user_choise])

computer_choose=random.randint(0,2)
print('Computer chooses:')
print(game_images[computer_choose])

if user_choise==0 and computer_choose==2:
    print("You win!")
elif computer_choose==0 and user_choise==2:
    print("You lose")
elif computer_choose>user_choise:
    print("You lose")
elif user_choise>computer_choose:
    print("You win!")
elif computer_choose==user_choise:
    print("It is a draw")
elif user_choise>=3 or user_choise<0:
    print("You typed an invalid number, so you loose the game")
