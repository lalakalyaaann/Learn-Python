import random

# Take a random word as a word to be guessed from the file
def load_words():
    with open("words.txt", "r") as file:
        # splitlines() splits the file into a list, where each line becomes one item
        #upper() reads the words from file in upper case 
        words = file.read().upper().splitlines()

    return words


# Choose a random word from the file
def choose_word(words):
    return random.choice(words)


# Display game rules
def display_rules():
    print("-" * 40)
    print("        WELCOME TO PYTHON WORDLE GAME")
    print("-" * 40)
    print("Guess the hidden 5-letter word.")
    print()
    print("Symbols:")
    print("✓ = Correct letter in correct position")
    print("* = Correct letter in wrong position")
    print(". = Letter not in word")
    print()
    print("You have 6 attempts.")
    print("-" * 40)


# Validate the user's guess
def is_valid_guess(guess, words):

    if guess == "":
        print("Input cannot be empty.")
        return False

    if not guess.isalpha():
        print("Only alphabetic letters are allowed.")
        return False

    if len(guess) != 5:
        print("Word must contain exactly 5 letters.")
        return False

    if guess not in words:
        print("Word not found in dictionary.")
        return False

    return True


# Compare the guessed word with the hidden word
def check_guess(guess, hidden_word):

    result = ""

    for i in range(5):
        if guess[i] == hidden_word[i]:
            result += "✓"
        elif guess[i] in hidden_word:
            result += "*"
        else:
            result += "."

    return result


# Main game function
def play_game():

    # Load words from file
    words = load_words()

    # Select a random hidden word
    hidden_word = choose_word(words)

    # Display game instructions
    display_rules()

    totalattempts = 6
    attempt = 1

    while attempt <= totalattempts:

        print(f"\nAttempt {attempt}/{totalattempts}")
        #Add remaining attempts.
        remaining_attempts = totalattempts - attempt + 1
        print(f"Remaining Attempts: {remaining_attempts}")

        # Take user input
        guess = input("Enter your guess: ").upper()

        # Validate input
        if not is_valid_guess(guess, words):
            continue

        # Check the guess
        result = check_guess(guess, hidden_word)

        print("Word Status:", result)

        # Win condition
        if guess == hidden_word:
            print(f"\n Congratulations! You guessed the word '{hidden_word}' in {attempt} attempts.")
            return

        attempt += 1

    # Lose condition
    print("\nGame Over!")
    print("The correct word was:", hidden_word)


# Call the function to play the game 


play_game()
#condition to ask the user to play again or not. 
while True:
    choice = input("\nDo you want to play again? (Y/N): ").strip().upper()

    if choice == "Y":
        print("\nStarting a new game...\n")
        play_game() #calls the game again if the user enters y.
        continue

    elif choice == "N":
        print("\nThank you for playing! Goodbye!") 
        break

    else:
        print("Please enter only Y or N.")
        
