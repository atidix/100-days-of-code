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

import random

player = int(input("Choose 0 for rock, 1 for paper, 2 for scissors\n"))

if player == 0:
  print(rock)
elif player == 1:
  print(paper)
elif player == 2:
  print(scissors)

rps = [0, 1, 2]

comp = random.choice(rps)

print("Computr chose:\n")

if comp == 0:
  print(rock)
elif comp == 1:
  print(paper)
elif comp == 2:
  print(scissors)

if player == comp:
  print("It's a draw")
elif player == 0 and comp == 1:
  print("You lose")
elif player == 0 and comp == 2:
  print("You win")
elif player == 1 and comp == 0:
  print("You win")
elif player == 1 and comp == 2:
  print("You lose")
elif player == 2 and comp == 0:
  print("You lose")
elif player == 2 and comp == 1:
  print("You win")
