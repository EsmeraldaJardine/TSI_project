from src.Hangman import *

class Game:
    def play_game(self):
        is_ready_to_play()
        selected_word = select_word()
        GUESSED_LETTERS.clear()
        hangman_drawings(WRONG_GUESSES_START)
        welcome_message(selected_word)
        
        victories = game_loop(selected_word, GUESSED_LETTERS, MAX_WRONG_GUESSES, WRONG_GUESSES_START)
        
        if victories == 1:
            game_result = "win"  

        else:
            game_result = "loss"

        is_playing = is_playing_again()

        return is_playing, game_result
                
