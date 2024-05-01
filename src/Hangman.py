from random import choice
import string
from src.HangmanDrawing import hangman_drawings

MAX_ATTEMPTS = 6

def welcome_message(selected_word):
    print("Welcome to Hangman!")
    print("You have 6 tries to guess the word.") 
    print("Good luck!")
    print("_ " * len(selected_word))


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


def join_guessed_letters(selected_word, guessed_letters):
    result = []
    for letter in selected_word:
        if letter in guessed_letters:
            result.append(letter)
        else:
            result.append('_')
    return ' '.join(result)

def is_gave_over(guessed_letters, selected_word, max_wrong_guesses, wrong_guesses):
    if wrong_guesses == max_wrong_guesses:
        print(f"Sorry! You have run out of tries. The word was: {selected_word}")
        return True
    if guessed_letters == set(selected_word):
        print(f"Congratulations! You have guessed the word: {selected_word}")
        return True
    return False
    

def game_loop(selected_word, guessed_letters, max_wrong_guesses, wrong_guesses):
    while is_gave_over(guessed_letters, selected_word, max_wrong_guesses, wrong_guesses) == False:
        player_input = get_player_input()
        if player_input in selected_word:
            guessed_letters.add(player_input)
            hangman_drawings(wrong_guesses)
            print(f"Correct! {join_guessed_letters(selected_word, guessed_letters)}")
            
        else:
            wrong_guesses += 1
            hangman_drawings(wrong_guesses)
            print(f"Incorrect! {join_guessed_letters(selected_word, guessed_letters)}")


#def main():
#    player_login = Login.LogIn()
#    selected_word = select_word()
#    guessed_letters = set()
#    max_wrong_guesses = MAX_ATTEMPTS
#    wrong_guesses = 0
#    hangman_drawings(wrong_guesses)
#    welcome_message(selected_word)
#    game_loop(selected_word, guessed_letters, max_wrong_guesses, wrong_guesses)
#
#main()