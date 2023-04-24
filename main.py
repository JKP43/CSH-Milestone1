
def main_menu(num):
    print("\nEnter 1 to play Guess the Number, 2 to play Rock Paper Scissors, 3 to play Hangman! "
          "\nYou can exit by entering 0 or 8 to return to this main screen")
    user_input = input()
    if user_input == '1':
        guessit(1)
    if user_input == '2':
        rps(2)
    if user_input == '3':
        hangman(3)
    if user_input == '0':
        exit()
    else:
        print("invalid input!\n")
        main_menu(user_input)

def guessit(num):
    print("\nGuess the Number!"
          "\nEnter to set range from 10 to 1000!"
          "\nI will respond whether the correct number is higher or lower!"
          "\nPress 8 to return to main screen to play a different game!")
    guess = input()
    if guess == '8':
        main_menu(guess)
    else:
        print("invalid input!")


def rps(num):
    print("\nLet's play Rock Paper Scissors!"
          "\nPress 1 for Rock, 2 for Paper, 3 for Scissors!"
          "\nPress 8 to return to main screen to play a different game!")
    decision = input()
    if decision == '8':
        main_menu(decision)
    else:
        print("invalid input!\n")

def hangman(num):
    print("\nHangman!")
    print("\n_ _ _ _ _")
    print("\nEnter an alphabet to start guessing!"
          "\nI will tell you whether the letter is included or not included!"
          "\nYou have 5 chances to correctly guess!"
          "\nPress 8 to return to main screen to play a different game!")
    letter = input()
    if letter == '8':
        main_menu(letter)
    else:
        print("invalid input!\n")

while True:
    print("\nEnter 1 to play Guess the Number, 2 to play Rock Paper Scissors, 3 to play Hangman! "
          "\nYou can exit by entering 0 or 8 to return to this main screen")
    user_input = input()
    if user_input == '1':
        guessit(1)
    if user_input == '2':
        rps(2)
    if user_input == '3':
        hangman(3)
    if user_input == '0':
        break
    else:
        print("invalid input!\n")
