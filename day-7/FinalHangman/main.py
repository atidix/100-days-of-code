import random
import hangman_words
import hangman_art

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6
i = 0

print(hangman_art.logo)

display = []
for _ in range(word_length):
    display += "_"
guessed_letters = []

while not end_of_game:
    i += 1
    guess = input("Guess a letter: ").lower()
    if guess in guessed_letters:
        print(f"You guessed {guess}. You have already guessed this letter.")
    
    for i in range(i):
        guessed_letters.append(guess)

    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:    
        lives -= 1
        print(f"You guessed {guess}. That's incorrect. You lose a life.")
    

        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(hangman_art.stages[lives])