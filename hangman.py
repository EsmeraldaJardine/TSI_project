from random import choice
import string

def select_word():
    with open("words.txt", mode="r") as words:
        word_list = words.readlines()
    return choice(word_list).strip()


def get_player_input():
    while True:
        player_input = input("Guess a new letter: ").lower()
        if validate_input(player_input):
            return player_input
        

def validate_input(player_input):
    if len(player_input) != 1:
        return False
    if player_input not in string.ascii_lowercase:
        return False
    return True


def join_guessed_letters(guessed_letters):
    return " ".join(sorted(guessed_letters))

def main():
    selected_word = select_word()
    guessed_letters = set()
    tries = 6
    print("Welcome to Hangman!")
    print("You have 6 tries to guess the word.") 
    print("Good luck!")
    print("_ " * len(selected_word))
    while tries > 0:
        player_input = get_player_input()
        if player_input in selected_word:
            guessed_letters.add(player_input)
            print(f"Correct! {join_guessed_letters(guessed_letters)}")
        else:
            tries -= 1
            print(f"Incorrect! {join_guessed_letters(guessed_letters)}")
            print(f"Tries left: {tries}")
        if guessed_letters == set(selected_word):
            print(f"Congratulations! You have guessed the word: {selected_word}")
            break
    else:
        print(f"Sorry! You have run out of tries. The word was: {selected_word}")

main()