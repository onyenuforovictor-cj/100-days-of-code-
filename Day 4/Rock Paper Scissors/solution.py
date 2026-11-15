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
game_image = [rock, paper, scissors]


user_input = int(input("welcome to Rock Paper Scissors. type '0' for rock, '1' for paper, '2' for scissors "))
while user_input <0 or user_input > 2:
    print("you have entered an invalid option try again")
    user_input = int(input("welcome to Rock Paper Scissors. type '0' for rock, '1' for paper, '2' for scissors "))
print("you choose")
print(game_image[user_input])

computer_choice = random.randint(0, 2)
print("computer chose:")
print(game_image[computer_choice])
if user_input == computer_choice:
    print("its a draw")
elif (user_input == 0 and computer_choice == 2
      or user_input == 1 and computer_choice == 0
      or  user_input == 2 and computer_choice == 1):
    print("you win")
else:
    print("you lose")


