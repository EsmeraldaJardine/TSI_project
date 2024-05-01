from src.Login import LogIn
from src.Hangman import *
from src.HangmanDrawing import hangman_drawings

class Main:
    def main():
        log_in = LogIn()
        log_in.log_in()
        selected_word = select_word()
        guessed_letters = set()
        max_wrong_guesses = MAX_ATTEMPTS
        wrong_guesses = 0
        hangman_drawings(wrong_guesses)
        welcome_message(selected_word)
        game_loop(selected_word, guessed_letters, max_wrong_guesses, wrong_guesses)

if __name__ == '__main__':
    Main.main()


