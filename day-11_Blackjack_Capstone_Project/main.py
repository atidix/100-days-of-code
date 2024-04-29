import random
from art import logo
import os
def clear():
    os.system('clear')

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def blackjack_game():

    def deal_card(cards):
        random_card = random.choice(cards)
        return random_card

    user_cards = []
    computer_cards = []

    user_cards.append(deal_card(cards))
    user_cards.append(deal_card(cards))

    computer_cards.append(deal_card(cards))
    computer_cards.append(deal_card(cards))


    def calculate_score(list_of_cards):
        if 11 in list_of_cards and sum(list_of_cards) > 21:
            list_of_cards.remove(11)
            list_of_cards.append(1)
        elif sum(list_of_cards) == 21:
            print("It's a blackjack!")
            return sum(list_of_cards)
        return sum(list_of_cards)

    print(f"Your cards are {user_cards} and your current score is: {calculate_score(user_cards)}")
    print(f"Computer's first card is {computer_cards[0]}")
    if sum(user_cards) == 21:
        print("It's a blackjack. You win!")
    elif sum(computer_cards) == 21:
        print("It's a blackjack. Computer wins!")
        

    else:
        game = True
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        
        while game:
            if user_score > 21:
                game = False
                break
            else:
                answer = input("Do you want to draw another card? 'y' or 'n'? ")
                if user_score < 21 and answer.lower() == 'y':
                    user_cards.append(deal_card(cards))
                    user_score = calculate_score(user_cards)
                    print(f"Your cards are now {user_cards} and your score is {user_score}")
                else:
                    game = False

        while computer_score < 17:
                        computer_cards.append(deal_card(cards))
                        computer_score = calculate_score(computer_cards)

        print(f"Your final hand is: {user_cards} and final score is: {user_score}")
        print(f"Computer's cards are: {computer_cards} and final score is: {computer_score}")
        

        def compare(user_score, computer_score):
            if user_score > 21:
                return "You went over. You lose!"
            elif computer_score > 21:
                return "Computer went over. You win!"
            elif user_score == computer_score:
                return "It's a draw"
            elif user_score > computer_score:
                return "You win!"
            else:
                return "You lose."
        print(compare(user_score, computer_score))    


restart = True
while restart:
    user_restart = input("Do you want to play a blackjack game? 'y' or 'n' ")
    if user_restart == 'n':
        restart = False
        print("Goodbye")
        clear()
    else:
         clear()
         print(logo)
         blackjack_game()



                
                    


            





   


