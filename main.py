import random
from hangman_art import stages,logo
with open("words.txt") as f:
    word_list = f.read().splitlines()
print(logo)
chosen_word = random.choice(word_list)

word_length = len(chosen_word)
#Creating "display" list to display dashes
display = []
lives = 6
game_finished = False

#Dashes will be equal to the length of the chosen word
for x in range(word_length):
    display += "_"

while not game_finished:
    guess = input("Guess a letter:").lower()

    if guess in display:
        print(f"You have already guessed {guess}")
        
    else:
        #this loop will go through each letter of chosen word, if the letter of the chosen word is same as the guess letter at a certain position, the letter will be added to the display list at that position
        for position in range(word_length):
          letter = chosen_word[position]
          if letter == guess:
              display[position] = letter
        print(f"{' '.join(display)}")

        if guess not in chosen_word:
            print(f"{guess} is not in the word. You lose a life")
            lives-=1
            if lives == 0:
                game_finished = True
                print("You lost")
                print(f"The word is {chosen_word}")

        if "_" not in display:
            game_finished = True
            print("You win!")
#prints the 'hanging' art from the list inside the file 'hangman_art'
        print(stages[lives])
    






