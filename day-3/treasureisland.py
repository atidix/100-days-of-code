print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
dir1 = input("You are a treasure hunter and you have to find the treasure. You are in the middle of the jungle and you have to pick which direction to go. You have to choose between 'left' or 'right'.\n")

dir = dir1.lower()

if dir == "left":
  print("You have now arrived at a lake. Do you choose to swim or go back in a different direction?")
  choice1 = input("Choose 'swim' or 'go back'\n")
  choice = choice1.lower()
  if choice == "go back":
    door1 = input("You go in a different direction and reach three doors. Which door do you choose? 'Red', 'Yellow' or 'blue'\n?")
    door = door1.lower()
    if door == "red":
      print("There is a fire behind the door. You are burned. Game over.\n")
    if door == "yellow":
      print("You have found the treasure. You win!\n")
    if door == "blue":
      print("There are wolves behind the door. You are eaten. Game over.\n")
    else:
      print("Game Over.")
  else:
    print("You are eaten by crocodiles. Game over.")