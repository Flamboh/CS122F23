"""
CS 122 Fall 2023 Project 5 Guess
Author: Oliver Boorstein
Credit:
Description: Write a program for a word guessing game
"""

# Function for word input
def input_guess_word():
    guess_word = input("Enter a guess word (blank to quit): ")
    if guess_word == "":
        quit()
    else:
        return guess_word

# Function to ask for letter input
def input_guess_letter():
    guess_letter = input("Enter a guess letter (blank to quit): ")
    if guess_letter == "":
        return False
    else:
        return guess_letter


# Function to display results of guess
def print_results(guess_word, guesses_matched, guesses_unmatched, guesses_total):
    print("\n*** Results ***")
    print(f"Word:\t\t {guess_word}")
    print(f"Matched:\t {guesses_matched}")
    print(f"Unmatched:\t {guesses_unmatched}")
    print(f"Guesses:\t {guesses_total}")


# Start function
def start():
    
    guesses_total = 0
    guesses_matched = ""
    guesses_unmatched = ""
    guesses_str = ""

    # Take input of word to guess and convert to lowercase
    guess_word = input_guess_word().lower()

    while True:
        guess_letter = input_guess_letter()
        # Check for blank input
        if guess_letter == False:
            if guesses_total > 0:
                print_results(guess_word, guesses_matched, guesses_unmatched, guesses_total)
            quit()
        # Convert letter to lowercase
        guess_letter = guess_letter.lower()
        # Check if guessing more than one letter
        if len(guess_letter) != 1:
            print("\t> Only enter a single letter")
        else:
            # Increment total guesses
            guesses_total += 1
            # Check for already guessed letter
            if guess_letter in guesses_str:
                if guess_letter in guess_word:
                    print(f"\t> {guess_letter} already guessed and found")
                    print(f"\t> Guesses so far: {guesses_str}")
                else:
                    print(f"\t> {guess_letter} already guessed and not found")
                    print(f"\t> Guesses so far: {guesses_str}")
            # Check if letter is in word
            elif guess_letter in guess_word:
                guesses_matched += guess_letter
                guesses_str += guess_letter
                print(f"\t> {guess_letter} found")
                print(f"\t> Guesses so far: {guesses_str}")
                # Check if letters in word to guess have been guessed
                correct_letters = 0
                for c in guess_word:
                    if c in guesses_str:
                        correct_letters += 1
                # If they all have been guessed break loop
                if correct_letters == len(guess_word):
                    print("\t> All letters found")
                    break
            # Else the letter was not in the word
            else:
                guesses_unmatched += guess_letter
                guesses_str += guess_letter
                print(f"\t> {guess_letter} not found")
                print(f"\t> Guesses so far: {guesses_str}")
    # Display results after loop has been broken
    print_results(guess_word, guesses_matched, guesses_unmatched, guesses_total)


start()