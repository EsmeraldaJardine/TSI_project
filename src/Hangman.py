from random import choice
import string
from src.HangmanDrawing import hangman_drawings
import getpass

MAX_WRONG_GUESSES = 6
GUESSED_LETTERS = set()
WRONG_GUESSES_START = 0

def is_ready_to_play():
    keyboard_input = getpass.getpass(prompt="\nPress ENTER to play: ")
    if keyboard_input in string.printable:
        return True

def welcome_message(selected_word):
    print("Let's Play Hangman!")
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
    if len(player_input) > 1: 
        print('Enter only a SINGLE character') 
        return False
    if player_input not in string.ascii_lowercase:
        print('Please only enter an alphabetic character') 
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


def is_game_over(guessed_letters, selected_word, max_wrong_guesses, wrong_guesses):
    wins = 0
    if wrong_guesses == max_wrong_guesses:
        print(f"Sorry! You have run out of tries. The word was: {selected_word}")
        return True, wins
    if guessed_letters == set(selected_word):
        print(f"Congratulations! You have guessed the word: {selected_word}")
        wins += 1
        return True, wins
    return False, wins
    
    
def is_playing_again():
    response = input("Play Again? (y/n): ").lower()
    if response == "y":
        print()
        print("_________________________")
        print("********NEW GAME********")
        return True
    elif response == "n":
        return False
    else:
        print("Invalid input. Please enter 'y' or 'n'")
        return is_playing_again()
    

def game_loop(selected_word, guessed_letters, max_wrong_guesses, wrong_guesses):
    victories = 0
    game_over = False
    while game_over == False:
        player_input = get_player_input()
        if player_input in selected_word:
            guessed_letters.add(player_input)
            hangman_drawings(wrong_guesses)
            print(f"Correct! {join_guessed_letters(selected_word, guessed_letters)}")
            
        else:
            wrong_guesses += 1
            hangman_drawings(wrong_guesses)
            print(f"Incorrect! {join_guessed_letters(selected_word, guessed_letters)}")
        
        game_over, wins = is_game_over(GUESSED_LETTERS, selected_word, max_wrong_guesses, wrong_guesses)
        if wins == 1:
            victories += 1
            
    return victories
       
    
            
            
