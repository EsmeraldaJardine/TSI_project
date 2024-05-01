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