import random

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', r'''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = [
    "aardvark", "baboon", "camel", "elephant", "giraffe", "hippo", 
    "iguana", "jaguar", "kangaroo", "koala", "lemur", "leopard", 
    "monkey", "orangutan", "panda", "penguin", "rhinoceros", 
    "tiger", "zebra", "badger", "beaver", "bison", "cheetah", 
    "donkey", "dolphin", "ferret", "flamingo", "gazelle", "gorilla", 
    "hyena", "jackal", "lizard", "meerkat", "ostrich", "peacock", 
    "quagga", "raccoon", "reindeer", "seal", "squirrel", "tapir", 
    "toucan", "walrus", "wombat", "yak"
]

def initialize_game():
    chosen_word = random.choice(word_list)
    answer = ["_"] * len(chosen_word)
    lives = 6
    return chosen_word, answer, lives

def display_intro():
    print(r'''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/             
      ''')

def hangman():
    while True:
        chosen_word, answer, lives = initialize_game()
        display_intro()
        print(stages[6])
        print("\nWelcome to Hangman Game !\n")
        print(" ".join(answer))

        end_of_game = False
        while not end_of_game:
            guess = input("\nGuess a letter: ").lower()
            
            if guess in answer:
                print(f"You've already guessed '{guess}'. Try another letter.")
                continue

            if guess not in chosen_word:
                lives -= 1
                print(stages[lives])
                print("Oops...Wrong letter!\n")

            for index, letter in enumerate(chosen_word):
                if letter == guess:
                    answer[index] = letter

            print(" ".join(answer))

            if "_" not in answer:
                end_of_game = True  
                print("\nCongratulations, you've won!")
                
            elif lives == 0:
                end_of_game = True  
                print("\nYou lost, Game Over.")
        
        restart = input('Would you like to restart the game? Type "yes" or "no": ').lower()
        if restart != "yes":
            print("Thanks for playing !")
            break

if __name__ == "__main__":
    hangman()
