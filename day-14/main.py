import random
import os
def clear():
    os.system('clear')
from game_data import data
from art import logo, vs


def random_entry():
    entry = random.choice(data)
    global f_count
    f_count = (int(entry['follower_count']))
    return (f"{entry['name']}, a {entry['description']}, from {entry['country']}.")

def game():
    game_continue = True
    Current_score = 0
    entry_A = random_entry()
    A = f_count
    entry_B = random_entry()
    B = f_count
    if entry_A == entry_B:
            entry_B = random_entry()
            B = f_count

    while game_continue:
        print(logo)            
        print(f"Compare A: {entry_A}")
        print (f"{vs}\n")
        print(f"Against B: {entry_B}\n")
        user_input = input("Who has more followers? Type 'A' or 'B': ").upper()
        clear()
        xyz = compare_entry(A, B, user_input)
        if xyz == 1:
            Current_score += 1
            print (f"You're right! Current score: {Current_score}")
            entry_A = entry_B
            A = B
            entry_B = random_entry()
            B = f_count 
        else:
            print(f"Sorry that was wrong. Your final score is {Current_score}")
            game_continue = False

def compare_entry(A, B, user_input):
    global answer
    answer = max(A,B)
    if user_input == 'A':
        user_input = A
    else:
        user_input = B
    
    if answer == user_input:
        return 1
    else:
        return 0
    
game()



    


