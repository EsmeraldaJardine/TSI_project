from src.Login import LogIn
from src.Hangman import *
from src.HangmanDrawing import hangman_drawings

class Main:
    def main():
        log_in = LogIn()
        log_in.log_in()
        while is_ready_to_play() == True:
            selected_word = select_word()
            hangman_drawings(WRONG_GUESSES_START)
            welcome_message(selected_word)
            game_loop(selected_word, GUESSED_LETTERS, MAX_ATTEMPTS, WRONG_GUESSES_START)
            if is_playing_again():
                continue
            else:
                break  

if __name__ == '__main__':
    Main.main()


