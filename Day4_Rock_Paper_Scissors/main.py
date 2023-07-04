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

#Write your code below this line 👇

game_images = [rock, paper, scissors]

player_choice = int(input("Select 0 for Rock, 1 for Paper, 2 for scissors: "))

player_image = game_images[player_choice]

computer_choice = random.randint(0,2)

computer_image = game_images[computer_choice]

print(f'You chose {player_image}')
print(f'The computer chose {computer_image}')

if player_choice == 0 and computer_choice == 2:
    print("You win")
elif player_choice == 2 and computer_choice == 0:
    print("You lose")
elif player_choice < computer_choice:
    print("You lost")
elif player_choice > computer_choice:
    print("You win!")
elif player_choice == computer_choice:
    print("It is a draw")

